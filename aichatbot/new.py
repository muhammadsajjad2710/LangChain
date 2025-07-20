# # `pip3 install assemblyai` (macOS)
# # `pip install assemblyai` (Windows)

# # import assemblyai as aai

# # aai.settings.api_key = "35f010c057384f079f110265d2c6a164"
# # transcriber = aai.Transcriber()

# # transcript = transcriber.transcribe("https://assembly.ai/news.mp4")
# # # transcript = transcriber.transcribe("./my-local-audio-file.wav")

# # print(transcript.text)

# import assemblyai as aai

# # Set your AssemblyAI API key
# aai.settings.api_key = "35f010c057384f079f110265d2c6a164"

# # Create a transcriber instance
# transcriber = aai.Transcriber()

# # Path to your local audio file
# audio_path = "D:/Artificial Intelligence/Lang chain/sampleaudio.mp4"

# # Transcribe the local file
# transcript = transcriber.transcribe(audio_path)

# # Print the transcribed text
# print("Transcribed Text:\n", transcript.text)

import assemblyai as aai
import openai
import json
import os

# Set API keys
aai.settings.api_key = "35f010c057384f079f110265d2c6a164"
openai.api_key = "sk-serviceid1-2go6zU6k1VTkacbDPXLaT3BlbkFJu4mQgl187uVNZUKP1yJC"



# Create a transcriber instance
transcriber = aai.Transcriber()

# Path to the audio file
audio_path = "C:Users\DELL\Downloads\Why Education.m4a"

# Check if the audio file exists
if not os.path.exists(audio_path):
    print("Error: Audio file not found.")
    exit()

# Transcribe the audio file
transcript = transcriber.transcribe(audio_path)

# Initialize OpenAI client
client = openai.OpenAI(api_key=openai.api_key)

# Send transcribed text to ChatGPT
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": transcript.text}
    ]
)

# Save output in JSON format in the same directory
script_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(script_dir, "output.json")

output_data = {
    "transcribed_text": transcript.text,
    "chatgpt_response": response.choices[0].message.content
}

with open(json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(output_data, json_file, ensure_ascii=False, indent=4)

print(f"Output saved to {json_file_path}")
