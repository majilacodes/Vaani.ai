# Vaani - The Future of Speech Translation

## 🌟 Overview
Welcome to **Vaani**, an innovative speech translation application that bridges language barriers through cutting-edge technology. Powered by OpenAI's Whisper model for speech recognition and Eleven Labs' advanced text-to-speech capabilities, Vaani transforms spoken words into translated audio, enabling seamless communication across different languages. Whether you're traveling, learning a new language, or connecting with friends from around the world, Vaani is your go-to solution for real-time translation.

## 🚀 Features
- **Intelligent Speech Recognition**: Harness the power of OpenAI's Whisper model to accurately transcribe spoken language into text, supporting multiple languages.
- **Dynamic Language Translation**: Effortlessly translate text between English and Tamil, ensuring that your message is conveyed accurately and effectively.
- **Natural Text-to-Speech**: Experience lifelike audio output with Eleven Labs' text-to-speech technology, making translations sound as natural as possible.
- **Real-Time Processing**: Enjoy instant feedback and translations with our Flask and SocketIO integration, designed for a smooth user experience.
- **User-Friendly Interface**: Navigate through a sleek and intuitive web interface that makes communication easy and enjoyable.

## 📋 Requirements
To get started with Vaani, ensure you have the following installed:
- **Python**: Version 3.x
- **Flask**: A lightweight WSGI web application framework.
- **Flask-SocketIO**: Enables real-time communication between clients and servers.
- **OpenAI Python Client**: For accessing OpenAI's API.
- **Requests**: For making HTTP requests.
- **Langdetect**: For language detection capabilities.

## 🛠️ Installation
Follow these simple steps to set up Vaani on your local machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/vaani.git
   cd vaani
   ```

2. **Install Required Packages**:
   Ensure you have `pip` installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys**:
   - Open `appdoning.py` and replace `YOUR_API_KEY` with your OpenAI API key.
   - Set your Eleven Labs credentials by replacing `YOUR_VOICE_ID` and `YOUR_API_KEY` in the same file.

## 🎤 Usage
Once you have Vaani set up, follow these steps to start translating:

1. **Launch the Flask Server**:
   ```bash
   python appdoning.py
   ```

2. **Access the Application**:
   Open your favorite web browser and navigate to `http://127.0.0.1:5000/`.

3. **Start Speaking**:
   Use the microphone feature to speak in your preferred language. Vaani will transcribe and translate your speech in real-time, providing audio output in the target language.

## 🤝 Contributing
We welcome contributions from the community! If you have ideas for new features, improvements, or bug fixes, please feel free to submit a pull request or open an issue. Together, we can make Vaani even better!

## 📄 License
This project is licensed under the MIT License. For more details, please refer to the [LICENSE](LICENSE) file.

## 🙏 Acknowledgments
A special thanks to:
- **OpenAI** for their groundbreaking Whisper model and ChatGPT technology.
- **Eleven Labs** for their exceptional text-to-speech API that brings our translations to life.
- **Flask** for providing a robust framework that powers our application.
- The open-source community for their invaluable contributions and support.

## 🌐 Connect with Us
Stay updated with the latest developments and join our community:
- [GitHub Repository](https://github.com/yourusername/vaani)
- [Twitter](https://twitter.com/yourusername)
- [LinkedIn](https://linkedin.com/in/yourusername)

---

Thank you for choosing Vaani! We hope it enhances your communication experience and opens up new opportunities for connection and understanding.