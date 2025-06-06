# import pytesseract
# from PIL import Image
# from gtts import gTTS
# from pydub import AudioSegment
# from pydub.playback import play
# import os
# import cv2

# def capture():
#     cap=cv2.VideoCapture(0)
#     while(True):
#         ret,frame=cap.read()
#         if not ret:
#             break
#         #frame=cv2.flip(frame,1)
#         cv2.resize(frame,(800,800))
#         if cv2.waitKey(1)==ord('q'):
#             break
#         cv2.imshow('newspaper',frame)
#         cv2.imwrite('./newspaper.jpg',frame)
    
#     cap.release()
#     cv2.destroyAllWindows()



# while True:
#     try:
#         capture()
#         text=pytesseract.image_to_string('./newspaper.jpg',lang='eng')
#         print(text)
#         tts = gTTS(text=text, lang='en')
#         tts.save("./output1.mp3")
#         play(AudioSegment.from_file('./output1.mp3'))
#         if os.path.exists('./output1.mp3'):
#             os.remove('./output1.mp3')
            
#             if os.path.exists('./newspaper.jpg'):
#                 os.remove('./newspaper.jpg')
#                 break
#     except:
#         tts = gTTS(text='try again', lang='en')
#         tts.save("./output2.mp3")
#         play(AudioSegment.from_file('./output2.mp3'))
        
#         if os.path.exists('./output2.mp3'):
#             os.remove('./output2.mp3')
#         continue
    



import cv2
import pytesseract
from PIL import Image
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

# Set the correct path for Tesseract (update this based on your installation)
pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"  # Update this path

def capture():
    cap = cv2.VideoCapture(0)  # Open the webcam

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Error: Failed to capture image")
            break

        frame = cv2.resize(frame, (800, 800))
        frame = cv2.flip(frame, 1)  # Flip for a natural mirror effect
        cv2.imshow('Press "q" to capture or "e" to exit', frame)

        key = cv2.waitKey(1)

        if key == ord('q'):  # Press 'q' to capture an image
            cv2.imwrite('./captured_text.jpg', frame)
            break
        elif key == ord('e'):  # Press 'e' to exit
            print("Exiting program...")
            cap.release()
            cv2.destroyAllWindows()
            exit()

    cap.release()
    cv2.destroyAllWindows()

while True:
    try:
        capture()
        
        if not os.path.exists('./captured_text.jpg'):
            continue  # If no image is captured, restart the loop
        
        text = pytesseract.image_to_string(Image.open('./captured_text.jpg'), lang='eng').strip()

        if text:
            print("📝 Extracted Text:\n", text)

            # Convert text to speech
            tts = gTTS(text=text, lang='en')
            tts.save("./output.mp3")
            play(AudioSegment.from_file('./output.mp3'))

        else:
            print("⚠️ No text detected. Try again.")
            tts = gTTS(text='No text detected, please try again.', lang='en')
            tts.save("./error.mp3")
            play(AudioSegment.from_file('./error.mp3'))

        # Cleanup files
        for file in ['./output.mp3', './error.mp3', './captured_text.jpg']:
            if os.path.exists(file):
                os.remove(file)

        break  # Exit loop after successful execution

    except Exception as e:
        print("❌ Error:", e)
        continue
