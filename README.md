# Web Palate - Voice Assistant Frontend

Frontend application for the TechGropse Voice Assistant.

## Backend Server
The backend server is already deployed at: `http://34.205.67.100:5000`

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

### Development Mode
```bash
python app.py
```
The server will run on `http://0.0.0.0:8080`

### Production Mode (Recommended)
```bash
gunicorn -w 4 -b 0.0.0.0:8080 app:app
```

### Run in Background
```bash
nohup gunicorn -w 4 -b 0.0.0.0:8080 app:app > frontend.log 2>&1 &
```

## Available Routes

- `/` - Main index page
- `/voice` - Voice-to-Voice interface
- `/text-voice` - Text-to-Voice interface
- `/text-chat` - Text-to-Text chat interface

## Deployment

For production deployment on a server:

1. Upload the entire `web_palate` directory to your server
2. Install dependencies: `pip install -r requirements.txt`
3. Run with gunicorn: `gunicorn -w 4 -b 0.0.0.0:80 app:app`
4. (Optional) Set up nginx as a reverse proxy
5. (Optional) Use systemd or supervisor to manage the process

## Port Configuration

- Frontend: Port 8080 (or 80 for production)
- Backend: Port 5000 (already running at 34.205.67.100)
