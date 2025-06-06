import cv2
from deepface import DeepFace

def detect_emotion_from_video():
    
    cap = cv2.VideoCapture(0)

    while True:
        
        ret, frame = cap.read()
        if not ret:
            break

       
        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            dominant_emotion = result[0]['dominant_emotion']

            cv2.putText(frame, f"Emotion: {dominant_emotion}", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        except Exception as e:
            print(f"Error detecting emotion: {e}")

       
        cv2.imshow('Emotion Detection', frame)

       
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

  
    cap.release()
    cv2.destroyAllWindows()
detect_emotion_from_video()
