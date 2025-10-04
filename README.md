# Smart Attendance System

A comprehensive attendance management system using QR codes and face recognition with automatic photo capture.

## Features

- **Student Registration**: Register students with face photos and generate QR codes
- **QR Code Attendance**: Scan QR codes to mark attendance with photo capture
- **Face Recognition Attendance**: Use face recognition to mark attendance with photo capture
- **Attendance Records**: View detailed attendance records with captured photos
- **Auto Photo Capture**: Automatically captures photos when marking attendance
- **Enhanced UI**: Beautiful interface with real-time metrics and status

## Installation

### Local Installation

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

## Deployment

### Railway Deployment (Recommended) 🚀

Railway is the recommended platform for this application as it supports the complex build requirements for face recognition.

1. **Sign up for Railway**: Go to [railway.app](https://railway.app)
2. **Connect GitHub**: Link your GitHub account
3. **Deploy from GitHub**:
   - Click "Deploy from GitHub repo"
   - Select your repository
   - Railway will auto-detect the project
4. **Deploy**: Railway will build and deploy automatically

**Railway Configuration:**
- **Requirements file**: `requirements.txt` (automatically detected)
- **Main file**: `app.py` (automatically detected)
- **Port**: Railway handles `$PORT` automatically
- **Configuration**: `railway.json` provides optimized settings

## Usage

1. **Register Students**: Go to "Register Student" and fill in student details with a face photo
2. **Mark Attendance**: Use either "QR Attendance" or "Face Attendance" to mark attendance
3. **View Records**: Check "View Attendance" to see all attendance records with photos

## Requirements

- Python 3.9+
- Webcam access for camera input
- All dependencies listed in `requirements.txt`

## File Structure

```
smart-attendance-System/
├── app.py                 # Main Streamlit application
├── db_utils.py           # Database utilities and functions
├── requirements.txt      # Python dependencies
├── railway.json          # Railway deployment configuration
├── README.md             # This file
├── .gitignore            # Git ignore rules
├── students.db           # SQLite database (created automatically)
├── qrcodes/              # Generated QR code images
├── encodings/            # Face encoding files
└── photos/               # Captured attendance photos
```

## Troubleshooting

### Railway Deployment Issues

#### Build Timeout
- **Error**: Build takes too long or times out
- **Solution**: Railway has generous build limits, but if issues persist, check the build logs for specific errors

#### Face Recognition Installation Issues
- **Error**: `dlib` or `face-recognition` installation fails
- **Solution**: Railway's build environment should handle this automatically. If issues persist, check the build logs

#### Memory Issues
- **Error**: Out of memory during build
- **Solution**: Railway provides adequate memory for builds. Contact Railway support if persistent issues occur

### Application Issues

- **Face Recognition Issues**: Ensure good lighting and clear face photos
- **QR Code Not Detected**: Make sure QR code is clearly visible and well-lit
- **Camera Access**: Grant camera permissions when prompted
- **Database Errors**: Ensure write permissions in the application directory

## Support

For issues or questions:
- Check the Railway build logs for deployment issues
- Check the application logs for runtime issues
- Contact Railway support for platform-specific problems

## License

This project is open source and available under the MIT License.