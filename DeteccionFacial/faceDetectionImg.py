# Docuemntación:
# soporta múltiples rostros, dectecta 6 puntos claves, 
# rápido y preciso
# Artículo de BlazeFace: https://arxiv.org/pdf/1907.05047.pdf }
# Cuadro delimitador para detectar el rostro


import cv2 as cv
import mediapipe as mp
import imutils 

mp_face_detection = mp.solutions.face_detection

#visualizar el rectarngulo y puntos clavesd
mp_drawing = mp.solutions.drawing_utils

with mp_face_detection.FaceDetection(
    # Valor mín de confianza para que una detección se determine como exitosa
    # se descartan de 0.5 o menos
    min_detection_confidence=0.5) as face_detection:
    img = cv.imread('DeteccionFacial/P_20211225_001347.jpg') 
    # Redimencionar imagen
    img = imutils.resize(img, width=500)

    # almacenar el alto y ancho
    height, width, _ = img.shape # los canales de color no hacen falta
    img_rgb =cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = face_detection.process(img_rgb)
    print("Detections:", results.detections)

    '''
    ##### PRIMERA PARTE ####
    # Dibujar los resultados con MediaPipe
    if results.detections is not None: #  evitar problemas con una imagen que no tenga rostros
        for detection in results.detections: #accesder a cada uno de los datos de cada detec
            mp_drawing.draw_detection(img, detection, # visualizar imagen y ver la información
            mp_drawing.DrawingSpec(color=(255,0,255), thickness=3, circle_radius=4),
            mp_drawing.DrawingSpec(color=(0,255,0), thickness=5)) # CUADRO DELIMITADOR
    ###############
    '''
    #### SEGUNDA PARTE ####
    # Acceder a las coordenadas de la imagen, acceder a la info de cada punto
    if results.detections is not None: 
        for detection in results.detections:
            # Bounding box
            xmin = int(detection.location_data.relative_bounding_box.xmin * width)
            ymin = int(detection.location_data.relative_bounding_box.ymin * height)
            w = int(detection.location_data.relative_bounding_box.width * width)
            h = int(detection.location_data.relative_bounding_box.height * height)
            print(xmin, ymin, w, h)
            # para verificar que esté bien
            cv.rectangle(img, (xmin, ymin), (xmin + w, ymin + h), (255,0,0), 2)

            # acceder a cada uno de los puntos claves
            # Ojo derecho, índice 0
            x_RE = int(detection.location_data.relative_keypoints[0].x * width)
            y_RE = int(detection.location_data.relative_keypoints[0].y * height)
            cv.circle(img, (x_RE, y_RE), 3, (0,0,255),2)

            # Ojo Izquierdo, 1
            x_LE = int(detection.location_data.relative_keypoints[1].x * width)
            y_LE = int(detection.location_data.relative_keypoints[1].y * height)
            cv.circle(img, (x_LE, y_LE), 3, (50,250,55),2)
            
            # Punta de la nariz
            x_NT = int(detection.location_data.relative_keypoints[2].x * width)
            y_NT = int(detection.location_data.relative_keypoints[2].y * height)
            cv.circle(img, (x_NT, y_NT), 3, (255,200,0),2)
            
            # Centro de la boca
            x_MC = int(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.MOUTH_CENTER).x * width)
            y_MC = int(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.MOUTH_CENTER).y * height)
            cv.circle(img, (x_MC, y_MC), 3, (255,50,50),2)

            # Trago de la oreja derecha
            x_RET = int(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.RIGHT_EAR_TRAGION).x * width)
            y_RET = int(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.RIGHT_EAR_TRAGION).y * height)
            cv.circle(img, (x_RET, y_RET), 3, (0,255,255),2)

            # Trago de la oreja IZQUIERDA
            x_LET = int(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.LEFT_EAR_TRAGION).x * width)
            y_LET = int(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.LEFT_EAR_TRAGION).y * height)
            cv.circle(img, (x_LET, y_LET), 3, (0,255,255),2)

    
    
    
    cv.imshow('Rostro', img)
    cv.waitKey(0)  
cv.destroyAllWindows()