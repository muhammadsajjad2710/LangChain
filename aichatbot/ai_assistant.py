import speech_recognition as sr
import openai
import subprocess
from pydub import AudioSegment

# Step 1: Convert audio from MP4 to WAV using ffmpeg
def convert_mp4_to_wav(mp4_path):
    wav_path = mp4_path.replace(".mp4", ".wav")
    # Run ffmpeg command to extract audio and convert to .wav
    subprocess.run(['ffmpeg', '-i', mp4_path, wav_path], check=True)
    return wav_path

# Step 2: Convert audio to text using SpeechRecognition
def audio_to_text(audio_path):
    wav_path = convert_mp4_to_wav(audio_path)  # Convert MP4 to WAV
    recognizer = sr.Recognizer()

    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)
        
    try:
        # Using Google Web Speech API for speech to text
        text = recognizer.recognize_google(audio_data)
        print("Transcribed text: ", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return ""
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return ""

# Step 3: Use OpenAI GPT-3 to get a response based on the text
def chatgpt_response(text):
    openai.api_key = 'your-openai-api-key-here'

    response = openai.Completion.create(
        engine="text-davinci-003",  # Or use another model depending on your needs
        prompt=text,
        max_tokens=150
    )

    return response.choices[0].text.strip()

# Main program
def main():
    audio_path = "D:/Artificial Intelligence/Lang chain/sampleaudio.mp4"
    transcribed_text = audio_to_text(audio_path)
    
    if transcribed_text:
        response = chatgpt_response(transcribed_text)
        print("ChatGPT response: ", response)

if __name__ == "__main__":
    main()
