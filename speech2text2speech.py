import os
from gtts import gTTS
import speech_recognition as sr

# Supported languages for both TTS and STT
LANGUAGES = {
    "en": "English (en-US)",
    "hi": "Hindi (hi-IN)",
    "mr": "Marathi(mr-IN)", 
    "gu": "Gujarati (gu-IN)",
    "te": "Telegu (te-IN)"
}

def display_languages():
    """Display supported languages."""
    print("Supported Languages:")
    for code, lang in LANGUAGES.items():
        print(f"{code}: {lang}")

def text_to_speech_gtts(text, language='en'):
    """
    Converts text to speech using gTTS and plays the audio.
    :param text: Text to convert to speech
    :param language: Language for TTS (e.g., 'en' for English, 'es' for Spanish)
    """
    try:
        tts = gTTS(text=text, lang=language, slow=False)
        audio_file = "speech_output.mp3"
        tts.save(audio_file)

        # Play the audio
        print("Playing audio...")
        os.system(f"start {audio_file}" if os.name == "nt" else f"open {audio_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def recognize_speech_from_mic(language_code="en-US"):
    """
    Captures audio from the microphone and converts it to text
    using Google's Speech Recognition API.
    """
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source)
            print(f"Listening for speech (Language: {LANGUAGES.get(language_code[:2], 'Unknown')}):")

            audio = recognizer.listen(source, timeout=10)
            print("Processing audio...")

            text = recognizer.recognize_google(audio, language=language_code)
            print(f"Recognized Text: {text}")
            return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from the API; {e}")
        return None
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
        return None


print("Multi-Language Speech-to-Text and Text-to-Speech Program Initialized!")
display_languages()

selected_language = input("\nEnter the language code (default: en): ").strip()
if selected_language not in LANGUAGES:
    print("Invalid or no input. Defaulting to English (en).")
    selected_language = "en"

language_code = f"{selected_language}-US" if selected_language != "hi" else "hi-IN"

while True:
    print("\nSelect an option:\n1. Speech-to-Text\n2. Text-to-Speech\n3. Quit")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        print("Speech-to-Text Mode Activated!")
        recognized_text = recognize_speech_from_mic(language_code=language_code)
        if recognized_text:
            print(f"Recognized Speech: {recognized_text}")
        else:
            print("No speech recognized.")

    elif choice == "2":
        print("Text-to-Speech Mode Activated!")
        text = input("Enter the text to convert to speech: ").strip()
        if text:
            text_to_speech_gtts(text, language=selected_language)
        else:
            print("No text provided.")

    elif choice == "3":
        print("Exiting program. Namaste Dhanyabad!")
        break

    else:
        print("Invalid choice. Please try again.")