# Smart Attendance System

A comprehensive attendance management system using QR codes and face recognition with automatic photo capture.

## Features

- **Student Registration**: Register students with face photos and generate QR codes
- **QR Code Attendance**: Scan QR codes to mark attendance with photo capture
- **Face Recognition Attendance**: Use face recognition to mark attendance with photo capture
- **Attendance Records**: View detailed attendance records with captured photos
- **Auto Photo Capture**: Automatically captures photos when marking attendance

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

### Cloud Deployment

#### Option 1: Streamlit Cloud (Recommended)
1. Push your code to GitHub
2. Connect to [Streamlit Cloud](https://share.streamlit.io)
3. **Use `requirements-simple.txt` for deployment** (QR code only)
4. **Set main file as `app-deploy.py`** (deployment-optimized version)
5. **OR use `requirements-minimal.txt` with `app.py`** (full features, may have build issues)

#### Option 2: Heroku
1. Use `requirements-deploy.txt`
2. Add `Procfile`:
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

#### Option 3: Railway (Full Features with Face Recognition) ⭐
1. **Use `requirements-railway.txt`**
2. **Use `app-railway.py` as main file**
3. **Railway will automatically detect and build the project**
4. **Includes face recognition and all features**

#### Option 4: Railway/Render (Alternative)
1. Use `requirements-minimal.txt`
2. Set start command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

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

### Railway Deployment (Recommended for Full Features) 🚀

1. **Sign up for Railway**: Go to [railway.app](https://railway.app)
2. **Connect GitHub**: Link your GitHub account
3. **Deploy from GitHub**:
   - Click "Deploy from GitHub repo"
   - Select your repository
   - Railway will auto-detect the project
4. **Configure Settings**:
   - **Requirements file**: `requirements-railway.txt`
   - **Main file**: `app-railway.py`
   - **Port**: Railway will set `$PORT` automatically
5. **Deploy**: Railway will build and deploy automatically

### Streamlit Cloud Deployment
1. Push your code to GitHub
2. Connect your GitHub repository to Streamlit Cloud
3. Deploy with the main file as `app.py`

## Troubleshooting

### Deployment Issues

#### Python Version Compatibility
- **Error**: `Requires-Python <3.13,>=3.9`
- **Solution**: Use Python 3.9-3.12 for deployment

#### Package Installation Errors
- **Error**: `No matching distribution found for numpy==1.26.0`
- **Solution**: Use `requirements-simple.txt` instead of `requirements.txt`

#### Build Compilation Errors
- **Error**: `Installing build dependencies` or numpy compilation fails
- **Solution**: 
  - Use `requirements-simple.txt` with `app-deploy.py` (QR code only)
  - This avoids face recognition packages that require compilation

#### Railway Deployment Issues
- **Error**: Build timeout or memory issues
- **Solution**: 
  - Railway has better build capabilities than Streamlit Cloud
  - Use `requirements-railway.txt` with `app-railway.py`
  - Railway supports face recognition compilation

#### Face Recognition Installation Issues
- **Error**: `dlib` installation fails
- **Solution**: 
  ```bash
  # For Ubuntu/Debian
  sudo apt-get install build-essential cmake
  sudo apt-get install libopenblas-dev liblapack-dev
  sudo apt-get install libx11-dev libgtk-3-dev
  sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
  ```

### Application Issues

- **Face Recognition Issues**: Ensure good lighting and clear face photos
- **QR Code Not Detected**: Make sure QR code is clearly visible and well-lit
- **Camera Access**: Grant camera permissions when prompted
- **Database Errors**: Ensure write permissions in the application directory

## Support

For issues or questions, please check the application logs or contact support."# smart-attendance-system-app" 
