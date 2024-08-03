import openai
import requests
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
from io import BytesIO
from langdetect import detect


# Set up OpenAI API
openai.api_key = 'YOUR_API_KEY'  # Replace with your actual OpenAI API key

# Eleven Labs API details
XI_API_KEY = "YOUR_API_KEY"  # Replace with your Eleven Labs API key
VOICE_ID = "YOUR_VOICE_ID"  # Replace with your voice ID from Eleven Labs
app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')

def speech_to_text(audio_bytes):
    audio_file = BytesIO(audio_bytes)
    audio_file.name = "audio.mp3"  # Provide a name attribute
    
    # Use OpenAI Whisper model for speech recognition
    response = openai.Audio.transcribe(
        model="whisper-1",
        file=audio_file,
        response_format="json"  # Change to JSON format
    )
    return response['text']

def translate_text(text, target_language):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a translator."},
            {"role": "user", "content": f"Translate the following text to {target_language}: {text}"}
        ]
    )
    return response.choices[0].message['content'].strip()

def text_to_speech(text):
    CHUNK_SIZE = 1024
    tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"
    
    headers = {
        "Accept": "application/json",
        "xi-api-key": XI_API_KEY
    }
    
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8,
            "style": 0.0,
            "use_speaker_boost": True
        }
    }
    
    response = requests.post(tts_url, headers=headers, json=data, stream=True)
    
    if response.ok:
        output = BytesIO()
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            output.write(chunk)
        output.seek(0)
        return output
    else:
        print(f"Failed to generate audio: {response.status_code}")
        print(response.text)
        return None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/newpage')
def new_page():
    return render_template('indexdoning.html')

@socketio.on('audio')
def handle_audio(data):
    audio_bytes = data['audio']
    recognized_text = speech_to_text(audio_bytes)
    
    if 'exit' in recognized_text.lower():
        emit('exit_response', {'message': 'Exiting...'})
        return
    
    detected_language = detect(recognized_text)
    target_language = 'Tamil' if detected_language == 'en' else 'English'
    
    translated_text = translate_text(recognized_text, target_language)
    audio_output = text_to_speech(translated_text)
    if audio_output:
        audio_output_bytes = audio_output.read()
        emit('audio_response', {'audio': audio_output_bytes, 'recognized_text': recognized_text, 'translated_text': translated_text})

if __name__ == '__main__':
    print("Starting Flask server...")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
    print("Flask server is running on http://127.0.0.1:5000/")
