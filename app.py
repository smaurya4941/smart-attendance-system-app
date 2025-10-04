import streamlit as st
from db_utils import init_db, add_student, fetch_student, fetch_attendance, mark_attendance, get_encoding
import numpy as np
import cv2
import face_recognition
from pyzbar.pyzbar import decode
from PIL import Image
import os

# ---------------- Streamlit UI ----------------
st.set_page_config(page_title="Smart Attendance App")
st.title("Smart Attendance App")

# Sidebar menu
menu = st.sidebar.radio("Go to", ["Home", "Register Student", "View Students",
                                  "QR Attendance", "Face Attendance", "View Attendance"])

# ---------------- Home ----------------
if menu == "Home":
    st.subheader("Welcome!")
    st.info("Smart Attendance App using QR and Face Recognition")

# ---------------- Register Student ----------------
elif menu == "Register Student":
    st.subheader("Register Student")
    with st.form("Register Form", clear_on_submit=True):
        name = st.text_input("Name")
        roll = st.text_input("Roll No")
        class_name = st.text_input("Class")
        img_file = st.file_uploader("Face Image", type=["jpg", "png", "jpeg"])
        submitted = st.form_submit_button("Register")
        if submitted:
            if name and roll and class_name and img_file:
                add_student(name, roll, class_name, img_file)
            else:
                st.warning("Fill all fields")

# ---------------- View Students ----------------
elif menu == "View Students":
    st.subheader("Students")
    students = fetch_student()
    if students:
        st.table(students)
    else:
        st.warning("No students found")

# ---------------- QR Attendance ----------------
elif menu == "QR Attendance":
    st.subheader("QR Attendance")
    img_file = st.camera_input("Scan QR Code")
    if img_file:
        try:
            img = Image.open(img_file)
            frame = np.array(img)
            decoded_objs = decode(frame)
            if decoded_objs:
                roll = decoded_objs[0].data.decode("utf-8")
                # Auto capture photo for attendance
                result = mark_attendance(roll, "QR", photo_data=img)
                st.success(result)
                
                # Show captured photo
                st.image(img, caption=f"Attendance Photo - {roll}", width=300)
            else:
                st.warning("No QR code detected")
        except Exception as e:
            st.error(f"Error processing QR code: {str(e)}")

# ---------------- Face Attendance ----------------
elif menu == "Face Attendance":
    st.subheader("Face Attendance")
    img_file = st.camera_input("Scan Face")
    if img_file:
        try:
            img = Image.open(img_file).resize((320, 240))
            frame = np.array(img)
            rgb_img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            face_encodings = face_recognition.face_encodings(rgb_img, face_recognition.face_locations(rgb_img))
            
            if not face_encodings:
                st.warning("No face detected in the image")
            else:
                found = False
                # Check if encodings directory exists and has files
                if not os.path.exists("encodings") or not os.listdir("encodings"):
                    st.warning("No student encodings found. Please register students first.")
                else:
                    for face_encoding in face_encodings:
                        for roll_file in os.listdir("encodings"):
                            if roll_file.endswith(".npy"):
                                roll = roll_file.replace(".npy", "")
                                known = get_encoding(roll)
                                if known is not None:
                                    matches = face_recognition.compare_faces([known], face_encoding)
                                    if matches[0]:
                                        # Auto capture photo for attendance
                                        result = mark_attendance(roll, "Face", photo_data=img)
                                        st.success(result)
                                        
                                        # Show captured photo
                                        st.image(img, caption=f"Attendance Photo - {roll}", width=300)
                                        found = True
                                        break
                        if found:
                            break
                    if not found:
                        st.warning("No matching face found")
        except Exception as e:
            st.error(f"Error processing face recognition: {str(e)}")

# ---------------- View Attendance ----------------
elif menu == "View Attendance":
    st.subheader("Attendance Records")
    attendance = fetch_attendance()
    if attendance:
        # Create a more detailed display with photos
        for record in attendance:
            name, roll, class_name, date, time, method, status, photo_path = record
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.write(f"**Name:** {name}")
                st.write(f"**Roll:** {roll}")
                st.write(f"**Class:** {class_name}")
                st.write(f"**Date:** {date}")
                st.write(f"**Time:** {time}")
                st.write(f"**Method:** {method}")
                st.write(f"**Status:** {status}")
            
            with col2:
                if photo_path and os.path.exists(photo_path):
                    st.image(photo_path, caption=f"Photo - {roll}", width=200)
                else:
                    st.write("No photo available")
            
            st.divider()
    else:
        st.warning("No records found")

# ---------------- Initialize DB ----------------
if __name__ == "__main__":
    init_db()