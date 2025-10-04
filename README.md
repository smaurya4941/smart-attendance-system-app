# Smart Attendance System

A comprehensive attendance management system using QR codes and face recognition with automatic photo capture.

## Features

- **Student Registration**: Register students with face photos and generate QR codes
- **QR Code Attendance**: Scan QR codes to mark attendance with photo capture
- **Face Recognition Attendance**: Use face recognition to mark attendance with photo capture
- **Attendance Records**: View detailed attendance records with captured photos
- **Auto Photo Capture**: Automatically captures photos when marking attendance

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd smart-attendance-System
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Register Students**: Go to "Register Student" and fill in student details with a face photo
2. **Mark Attendance**: Use either "QR Attendance" or "Face Attendance" to mark attendance
3. **View Records**: Check "View Attendance" to see all attendance records with photos

## Requirements

- Python 3.8+
- Webcam access for camera input
- All dependencies listed in `requirements.txt`

## File Structure

```
smart-attendance-System/
├── app.py                 # Main Streamlit application
├── db_utils.py           # Database utilities and functions
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── students.db           # SQLite database (created automatically)
├── qrcodes/              # Generated QR code images
├── encodings/            # Face encoding files
└── photos/               # Captured attendance photos
```

## Deployment

### Local Deployment
```bash
streamlit run app.py
```

### Cloud Deployment (Streamlit Cloud)
1. Push your code to GitHub
2. Connect your GitHub repository to Streamlit Cloud
3. Deploy with the main file as `app.py`

## Troubleshooting

- **Face Recognition Issues**: Ensure good lighting and clear face photos
- **QR Code Not Detected**: Make sure QR code is clearly visible and well-lit
- **Camera Access**: Grant camera permissions when prompted

## Support

For issues or questions, please check the application logs or contact support."# smart-attendance-system-app" 
