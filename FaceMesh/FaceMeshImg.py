# Ofrece 468 puntos en el rostro 3D en tiempo real
#dibujar
# no es necesario un sensor de profundidad
# Dos modelos de redes neuronales profundas

# Face  LandMark Model, se basan mediante el fotograma anterior
# cuando no se haya identificado la presencia de la cara
# https://google.github.io/mediapipe/solutions/face_mesh

import cv2 as cv
import mediapipe as mp
import imutils
import pandas as pd # para convertir a lista

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

##### Después de obtener 1 punto ####
index_list = [70,63,105,66,107,336,296,334,293,300,
                122,196,3,51,281,248,419,351,37,0,267]

with mp_face_mesh.FaceMesh(
    static_image_mode=True,
    max_num_faces=1,
    min_detection_confidence=0.5) as face_mesh:

    img = cv.imread('P_20211225_001347.jpg')
    img = imutils.resize(img, width=500)

    height, width, _ = img.shape
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = face_mesh.process(img_rgb)

    # print('Face landmarks', results.multi_face_landmarks)
    '''
    if results.multi_face_landmarks is not None:
        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(img, face_landmarks,
                mp_face_mesh.FACEMESH_CONTOURS,
                mp_drawing.DrawingSpec(color=(0,255,255), thickness=1, circle_radius=1),
                mp_drawing.DrawingSpec(color=(255,0,255), thickness=1))
    '''

    if results.multi_face_landmarks is not None:
        x_list = []
        y_list = []
        for face_landmarks in results.multi_face_landmarks:
        
            """ x = int(face_landmarks.landmark[4].x * width)
            y = int(face_landmarks.landmark[4].y * height)
            cv.circle(img, (x,y), 2, (255,255,0), 2)
            
            """

            # Acceder a 21 puntos
            for index in index_list:
                x = int(face_landmarks.landmark[index].x * width)
                y = int(face_landmarks.landmark[index].y * height)
                cv.circle(img, (x, y), 2, (255,0,255),2)

                # se hace al finalizar la detección,
                x_list.append(x)
                y_list.append(y)
            # al final
            xy_list = pd.DataFrame({"X: ": x_list, "Y: ": y_list}) 
          
            cv.imshow('Img', img)
            cv.waitKey(0)
        
        ###  GUARDAR DATOS EN UN TXT
        fichero = open("./Ficheros/MeshImg.txt", "w", encoding='utf-8')
        with fichero as file_object:
            file_object.write(str(xy_list)) 
            # file_object.write(str(x_list) + str(y_list).rjust(5)+"\n") 
        fichero.close()
                


    cv.imshow('Img', img)
    cv.waitKey(0)
    
cv.destroyAllWindows()