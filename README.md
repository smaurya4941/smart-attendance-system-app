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

### Render.com Deployment (FREE) 🆓

Render is the best free platform for this application as it supports complex builds including face recognition.

#### Step-by-Step Deployment:

1. **Sign up for Render**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub account

2. **Create Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select your repository

3. **Configure Settings**
   - **Name**: `smart-attendance-system` (or your preferred name)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true`
   - **Python Version**: `3.11.0`

4. **Advanced Settings**
   - **Auto-Deploy**: Yes (deploys automatically on git push)
   - **Health Check Path**: `/` (optional)

5. **Deploy**
   - Click "Create Web Service"
   - Render will build and deploy automatically
   - Build time: ~10-15 minutes (face recognition compilation)

#### Render Configuration:
- **Requirements file**: `requirements.txt`
- **Main file**: `app.py`
- **Procfile**: `Procfile` (for start command)
- **Free tier**: 750 hours/month, 512MB RAM
- **Build time**: Up to 45 minutes

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
├── requirements.txt      # Python dependencies for Render
├── Procfile              # Render start command
├── README.md             # This file
├── students.db           # SQLite database (created automatically)
├── qrcodes/              # Generated QR code images
├── encodings/            # Face encoding files
└── photos/               # Captured attendance photos
```

## Troubleshooting

### Render Deployment Issues

#### Build Timeout
- **Error**: Build takes too long or times out
- **Solution**: Render allows up to 45 minutes for builds. Face recognition compilation can take 10-15 minutes.

#### Face Recognition Installation Issues
- **Error**: `dlib` or `face-recognition` installation fails
- **Solution**: Render's build environment handles this automatically. Check build logs for specific errors.

#### Memory Issues
- **Error**: Out of memory during build
- **Solution**: Render provides 512MB RAM which is sufficient. If issues persist, check build logs.

#### Service Not Starting
- **Error**: Service fails to start
- **Solution**: Check that `Procfile` is present and start command is correct.

### Application Issues

- **Face Recognition Issues**: Ensure good lighting and clear face photos
- **QR Code Not Detected**: Make sure QR code is clearly visible and well-lit
- **Camera Access**: Grant camera permissions when prompted
- **Database Errors**: Ensure write permissions in the application directory

## Support

For issues or questions:
- Check the Render build logs for deployment issues
- Check the application logs for runtime issues
- Contact Render support for platform-specific problems

## License

This project is open source and available under the MIT License.