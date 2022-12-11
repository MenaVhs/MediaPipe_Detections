import cv2 as cv
import mediapipe as mp
import pandas as pd

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
cap.set(cv.CAP_PROP_FPS, 5)

index_list = [70,63,105]

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

with mp_face_mesh.FaceMesh(
    static_image_mode = True, 
    max_num_faces=1, 
    min_detection_confidence = 0.5) as face_mesh:

    while True:
        ret, frame = cap.read()
        
        if ret == False:
            break

        frame = cv.flip(frame, 3)
        frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        
        height, width, _ = frame.shape
        
        results = face_mesh.process(frame_rgb)

        if results.multi_face_landmarks is not None:
            x_list = []
            y_list = []
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(frame, face_landmarks, 
                mp_face_mesh.FACEMESH_CONTOURS,
                mp_drawing.DrawingSpec(color=(0,255,255), thickness=1, circle_radius = 1),
                mp_drawing.DrawingSpec(color=(255,0, 255), thickness=1))
                print("Hola\t")
                for index in index_list:
                    #print(index)
                    x = int(face_landmarks.landmark[index].x * width)
                    y = int(face_landmarks.landmark[index].y * height)
                    cv.circle(frame, (x, y), 2, (255,0,255), 2)

                    x_list.append(x)
                    y_list.append(y)
                    

                    print(index, x, y)
                    
                xy_list = pd.DataFrame({"X: ": x_list, "Y: ": y_list})

            cv.imshow('Frame', frame)
            k = cv.waitKey(1) & 0xFF
            if k == 115:
                break
        
        ### Guardar en fichero
        fichero = open("./Ficheros/MeshVideo.txt", "w", encoding='utf-8')
        with fichero as file_object:
            file_object.write(str(xy_list))
        fichero.close()



cap.realise()
cv.destroyAllWindows()
