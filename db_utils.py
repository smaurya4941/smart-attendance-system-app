import os
from datetime import datetime
import sqlite3
import qrcode
import numpy as np
import face_recognition
from PIL import Image
import cv2
import streamlit as st

# Setup folders
os.makedirs("qrcodes", exist_ok=True)
os.makedirs("encodings", exist_ok=True)
os.makedirs("photos", exist_ok=True)

# ---------------- Database ----------------
def init_db():
    db = sqlite3.connect("students.db")
    cur = db.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll TEXT UNIQUE NOT NULL,
            class TEXT NOT NULL
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS attendance(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            date TEXT,
            time TEXT,
            method TEXT,
            status TEXT NOT NULL,
            photo_path TEXT,
            FOREIGN KEY(student_id) REFERENCES students(id)
        )
    ''')
    db.commit()
    db.close()

# ---------------- Add Student ----------------
def add_student(name, roll, class_name, img_file):
    db = sqlite3.connect("students.db")
    cur = db.cursor()
    try:
        cur.execute("INSERT INTO students (name, roll, class) VALUES (?, ?, ?)",
                    (name, roll, class_name))
        db.commit()

        # QR Code
        qr = qrcode.make(roll)
        qr.save(f"qrcodes/{roll}.png")

        # Face Encoding (resize image to reduce memory)
        if img_file:
            img = Image.open(img_file)
            img = img.resize((320, 240))
            img_array = np.array(img)
            rgb_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
            encodings = face_recognition.face_encodings(rgb_img)
            if encodings:
                np.save(f"encodings/{roll}.npy", encodings[0])
                st.success("Face encoding saved")
            else:
                st.warning("No face detected")
        st.success(f"Student {name} added successfully!")
    except sqlite3.IntegrityError:
        st.error("Roll number already exists")
    finally:
        db.close()

# ---------------- Fetch Students & Attendance ----------------
def fetch_student():
    db = sqlite3.connect("students.db")
    cur = db.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    db.close()
    return rows

def fetch_attendance():
    db = sqlite3.connect("students.db")
    cur = db.cursor()
    cur.execute("""
        SELECT s.name, s.roll, s.class, a.date, a.time, a.method, a.status, a.photo_path
        FROM attendance a
        JOIN students s ON a.student_id = s.id
        ORDER BY a.date DESC, a.time DESC
    """)
    rows = cur.fetchall()
    db.close()
    return rows

# ---------------- Mark Attendance ----------------
def mark_attendance(roll, method, photo_data=None):
    db = sqlite3.connect("students.db")
    cur = db.cursor()
    cur.execute("SELECT id FROM students WHERE roll=?", (roll,))
    student = cur.fetchone()
    if not student:
        db.close()
        return f"Student {roll} not found!"

    student_id = student[0]
    today = datetime.now().strftime("%Y-%m-%d")
    now = datetime.now().strftime("%H:%M:%S")

    cur.execute("SELECT * FROM attendance WHERE student_id=? AND date=?", (student_id, today))
    if not cur.fetchone():
        # Save photo if provided
        photo_path = None
        if photo_data:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            photo_filename = f"{roll}_{timestamp}.jpg"
            photo_path = f"photos/{photo_filename}"
            
            # Convert photo data to PIL Image and save
            if isinstance(photo_data, np.ndarray):
                img = Image.fromarray(photo_data)
            else:
                img = photo_data
            img.save(photo_path)
        
        cur.execute("INSERT INTO attendance (student_id, date, time, method, status, photo_path) VALUES (?, ?, ?, ?, ?, ?)",
                    (student_id, today, now, method, "Present", photo_path))
        db.commit()
        status = f"Attendance marked for roll {roll} via {method}"
    else:
        status = f"Attendance already marked today"

    db.close()
    return status

# ---------------- Lazy Loading Face Encodings ----------------
def get_encoding(roll):
    path = f"encodings/{roll}.npy"
    if os.path.exists(path):
        return np.load(path)
    return None