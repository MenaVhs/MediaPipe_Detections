import cv2 as cv
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

# detector de rostros
with mp_face_detection.FaceDetection(
    min_detection_confidence=0.5) as face_detection:

    while True: 
        ret, frame = cap.read()
        if ret == False:
            break
        frame = cv.flip(frame, 1)
        frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = face_detection.process(frame_rgb)

        if results.detections is not None:
            for detection in results.detections:
                mp_drawing.draw_detection(frame ,detection, 
                    mp_drawing.DrawingSpec(color=(0,255,255), circle_radius=5),
                    mp_drawing.DrawingSpec(color=(255,0,255)))

        cv.imshow('Frame', frame)
        k = cv.waitKey(1) & 0xFF
        if k == 115:
            break

    cap.realise()
    cv.destroyAllWindows()
