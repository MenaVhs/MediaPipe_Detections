import cv2 as cv
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

with mp_face_mesh.FaceMesh(
    static_image_mode=True,
    max_num_faces=1,
    min_detection_confidence=0.5) as face_mesh:

    while True: 
        ret, frame = cap.read()
        if ret == False:
            break
        frame = cv.flip(frame, 1)
        frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = face_mesh.process(frame_rgb)

        if results.multi_face_landmarks is not None:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(frame, face_landmarks,
                    mp_face_mesh.FACEMESH_CONTOURS,
                    mp_drawing.DrawingSpec(color=(0,255,255), thickness=1, circle_radius=1),
                    mp_drawing.DrawingSpec(color=(255,0,255), thickness=1))
        
        cv.imshow('Frame', frame)
        k = cv.waitKey(1) & 0xFF
        if k == 115:
            break