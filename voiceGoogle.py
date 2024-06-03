import speech_recognition as sr 

import pyttsx3 
engine = pyttsx3.init()

import os

import google.generativeai as genai

genai.configure(api_key="AIzaSyC7YdNU_9edgcst1KnU9h9Ye9wIdxTXBpc")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "hello\n\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Hello! What can I do for you today? \n",
      ],
    },
  ]
)



def recognize_speech_from_mic(duration=5):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Adjusting for ambient noise... please wait.")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for speech...")
        audio = recognizer.listen(source, timeout=duration)

    print("Recognizing speech...")
    try:
        transcription = recognizer.recognize_google(audio)
        print("you said: " + transcription)

        response = chat_session.send_message(f"limit to 100 words \n {transcription}")
        print(response.text)
        engine.say(response.text)
        engine.runAndWait()
    except sr.RequestError:
        print("API was unreachable or unresponsive")
    except sr.UnknownValueError:
        print("Unable to recognize speech")

if __name__ =="__main__":
    recognize_speech_from_mic()