#!/usr/bin/env python3
"""
Smart Attendance System - Deployment Script
Run this script to start the application
"""

import subprocess
import sys
import os

def check_requirements():
    """Check if all required packages are installed"""
    try:
        import streamlit
        import cv2
        import face_recognition
        import qrcode
        import numpy
        from PIL import Image
        from pyzbar import pyzbar
        print("✅ All required packages are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def main():
    """Main deployment function"""
    print("🚀 Starting Smart Attendance System...")
    
    # Check if we're in the right directory
    if not os.path.exists("app.py"):
        print("❌ app.py not found. Please run this script from the project directory.")
        sys.exit(1)
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    # Start the application
    print("📱 Starting Streamlit application...")
    print("🌐 The app will open in your browser at http://localhost:8501")
    print("📷 Make sure your camera is accessible for attendance marking")
    print("⏹️  Press Ctrl+C to stop the application")
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"], check=True)
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
