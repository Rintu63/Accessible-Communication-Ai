from ultralytics import YOLO  
import cv2
import pyttsx3

def detect_objects_realtime():
    
    tts_engine = pyttsx3.init()
    tts_engine.setProperty('rate', 150)  
    tts_engine.setProperty('volume', 0.9)  

    
    model = YOLO("yolo11n.pt")  

    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Press 'q' to exit the webcam.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        results = model.predict(source=frame, conf=0.25, show=False, imgsz=640) 
        annotated_frame = results[0].plot()  
        detected_objects = [model.names[int(cls)] for cls in results[0].boxes.cls]
        if detected_objects:
            objects_text = ", ".join(detected_objects)
            print(f"Detected: {objects_text}")
            if not tts_engine._inLoop:  
                tts_engine.say(f"Detected: {objects_text}")
                tts_engine.runAndWait()

        cv2.imshow("YOLOv11 Real-Time Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Webcam released and resources cleared")

if __name__ == "__main__":
    detect_objects_realtime()
