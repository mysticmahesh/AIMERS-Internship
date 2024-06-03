import speech_recognition as sr

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
    except sr.RequestError:
        print("API was unreachable or unresponsive")
    except sr.UnknownValueError:
        print("Unable to recognize speech")

if __name__ =="__main__":
    recognize_speech_from_mic()
