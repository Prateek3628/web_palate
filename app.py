from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, 
            template_folder='templates',
            static_folder='static')

@app.route('/')
def index():
    """Serve the main index page"""
    return render_template('index.html')

@app.route('/voice')
def voice_to_voice():
    """Serve the voice-to-voice interface"""
    return send_from_directory('static', 'voice_to_voice.html')

@app.route('/text-voice')
def text_to_voice():
    """Serve the text-to-voice interface"""
    return send_from_directory('static', 'text_to_voice.html')

@app.route('/text-chat')
def text_to_text():
    """Serve the text-to-text chat interface"""
    return send_from_directory('static', 'text_to_text.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serve static files"""
    return send_from_directory('static', filename)

if __name__ == '__main__':
    # Run on all interfaces, port 8080
    # For production, use gunicorn or uwsgi
    app.run(host='0.0.0.0', port=8080, debug=False)
