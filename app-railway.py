import streamlit as st
from db_utils import init_db, add_student, fetch_student, fetch_attendance, mark_attendance, get_encoding
import numpy as np
import cv2
import face_recognition
from pyzbar.pyzbar import decode
from PIL import Image
import os

# Railway-specific configuration
if os.getenv('RAILWAY_ENVIRONMENT'):
    st.set_page_config(
        page_title="Smart Attendance App",
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="expanded"
    )
else:
    st.set_page_config(page_title="Smart Attendance App")

st.title("🎓 Smart Attendance System")
st.markdown("**QR Code & Face Recognition Attendance Management**")

# Sidebar menu
menu = st.sidebar.radio("Navigate", ["🏠 Home", "👤 Register Student", "📋 View Students",
                                    "📱 QR Attendance", "👁️ Face Attendance", "📊 View Attendance"])

# ---------------- Home ----------------
if menu == "🏠 Home":
    st.subheader("Welcome to Smart Attendance System!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Features:**
        - 📱 QR Code Attendance
        - 👁️ Face Recognition
        - 📸 Auto Photo Capture
        - 📊 Attendance Reports
        - 👤 Student Management
        """)
    
    with col2:
        st.success("""
        **How to Use:**
        1. Register students with photos
        2. Generate QR codes automatically
        3. Mark attendance via QR or face
        4. View detailed reports
        """)
    
    # Show system status
    st.subheader("System Status")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Students Registered", len(fetch_student()))
    
    with col2:
        attendance_count = len(fetch_attendance())
        st.metric("Total Attendance Records", attendance_count)
    
    with col3:
        if os.path.exists("encodings"):
            encoding_count = len([f for f in os.listdir("encodings") if f.endswith(".npy")])
            st.metric("Face Encodings", encoding_count)
        else:
            st.metric("Face Encodings", 0)

# ---------------- Register Student ----------------
elif menu == "👤 Register Student":
    st.subheader("Register New Student")
    
    with st.form("Register Form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name", placeholder="Enter student's full name")
            roll = st.text_input("Roll Number", placeholder="Enter unique roll number")
        
        with col2:
            class_name = st.text_input("Class", placeholder="Enter class/section")
            img_file = st.file_uploader("Student Photo", type=["jpg", "png", "jpeg"], 
                                      help="Upload a clear photo of the student's face")
        
        submitted = st.form_submit_button("Register Student", use_container_width=True)
        
        if submitted:
            if name and roll and class_name and img_file:
                with st.spinner("Registering student..."):
                    add_student(name, roll, class_name, img_file)
            else:
                st.warning("⚠️ Please fill in all fields and upload a photo")

# ---------------- View Students ----------------
elif menu == "📋 View Students":
    st.subheader("Registered Students")
    
    students = fetch_student()
    if students:
        # Create a more detailed table
        st.dataframe(
            students,
            column_config={
                "id": "ID",
                "name": "Name",
                "roll": "Roll Number",
                "class": "Class"
            },
            use_container_width=True
        )
        
        # Show QR codes if available
        if st.checkbox("Show QR Codes"):
            cols = st.columns(min(len(students), 3))
            for i, student in enumerate(students):
                with cols[i % 3]:
                    roll = student[2]  # roll is at index 2
                    qr_path = f"qrcodes/{roll}.png"
                    if os.path.exists(qr_path):
                        st.image(qr_path, caption=f"QR Code - {student[1]}", width=150)
    else:
        st.warning("No students registered yet. Please register students first.")

# ---------------- QR Attendance ----------------
elif menu == "📱 QR Attendance":
    st.subheader("Mark Attendance via QR Code")
    
    st.info("📱 Use your camera to scan the student's QR code")
    
    img_file = st.camera_input("Scan QR Code", key="qr_camera")
    
    if img_file:
        try:
            with st.spinner("Processing QR code..."):
                img = Image.open(img_file)
                frame = np.array(img)
                decoded_objs = decode(frame)
                
                if decoded_objs:
                    roll = decoded_objs[0].data.decode("utf-8")
                    
                    # Show the scanned QR code
                    st.image(img, caption=f"Scanned QR Code - Roll: {roll}", width=300)
                    
                    # Mark attendance
                    result = mark_attendance(roll, "QR", photo_data=img)
                    st.success(result)
                    
                else:
                    st.warning("❌ No QR code detected. Please ensure the QR code is clearly visible.")
                    
        except Exception as e:
            st.error(f"Error processing QR code: {str(e)}")

# ---------------- Face Attendance ----------------
elif menu == "👁️ Face Attendance":
    st.subheader("Mark Attendance via Face Recognition")
    
    st.info("👁️ Use your camera to scan the student's face")
    
    img_file = st.camera_input("Scan Face", key="face_camera")
    
    if img_file:
        try:
            with st.spinner("Processing face recognition..."):
                img = Image.open(img_file).resize((320, 240))
                frame = np.array(img)
                rgb_img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                face_encodings = face_recognition.face_encodings(rgb_img, face_recognition.face_locations(rgb_img))
                
                if not face_encodings:
                    st.warning("❌ No face detected in the image. Please ensure the face is clearly visible.")
                else:
                    found = False
                    
                    # Check if encodings directory exists and has files
                    if not os.path.exists("encodings") or not os.listdir("encodings"):
                        st.warning("⚠️ No student encodings found. Please register students first.")
                    else:
                        for face_encoding in face_encodings:
                            for roll_file in os.listdir("encodings"):
                                if roll_file.endswith(".npy"):
                                    roll = roll_file.replace(".npy", "")
                                    known = get_encoding(roll)
                                    if known is not None:
                                        matches = face_recognition.compare_faces([known], face_encoding)
                                        if matches[0]:
                                            # Show the captured image
                                            st.image(img, caption=f"Recognized Face - Roll: {roll}", width=300)
                                            
                                            # Mark attendance
                                            result = mark_attendance(roll, "Face", photo_data=img)
                                            st.success(result)
                                            found = True
                                            break
                            if found:
                                break
                        
                        if not found:
                            st.warning("❌ No matching face found. Please ensure the student is registered.")
                            
        except Exception as e:
            st.error(f"Error processing face recognition: {str(e)}")

# ---------------- View Attendance ----------------
elif menu == "📊 View Attendance":
    st.subheader("Attendance Records")
    
    attendance = fetch_attendance()
    if attendance:
        # Create a more detailed display with photos
        for record in attendance:
            name, roll, class_name, date, time, method, status, photo_path = record
            
            with st.container():
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown(f"""
                    **👤 {name}** | **🎓 Roll: {roll}** | **📚 Class: {class_name}**
                    
                    📅 **Date:** {date} | ⏰ **Time:** {time} | 🔧 **Method:** {method} | ✅ **Status:** {status}
                    """)
                
                with col2:
                    if photo_path and os.path.exists(photo_path):
                        st.image(photo_path, caption=f"Photo - {roll}", width=150)
                    else:
                        st.write("📷 No photo available")
                
                st.divider()
    else:
        st.warning("No attendance records found.")

# ---------------- Initialize DB ----------------
if __name__ == "__main__":
    init_db()
