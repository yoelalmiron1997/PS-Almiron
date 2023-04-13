import cv2

cars_detec = cv2.CascadeClassifier('cars.xml')
cap1 = cv2.VideoCapture('video1.avi')
cap2 = cv2.VideoCapture('video2.avi')

face_count1 = 0
face_count2 = 0
count1 = 0
count2 = 0

font_scale = 1
font_thickness = 2
font_face = cv2.FONT_HERSHEY_SIMPLEX
text_color = (0, 255, 0)

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    
    if not ret1 or not ret2:
        break
    
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    
    faces1 = cars_detec.detectMultiScale(gray1, 1.1, 4)
    faces2 = cars_detec.detectMultiScale(gray2, 1.1, 4)
    
    count1 += len(faces1)
    count2 += len(faces2)
    
    for (x, y, w, h) in faces1:
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
    for (x, y, w, h) in faces2:
        cv2.rectangle(frame2, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    if count1 >= 10:
        face_count1 += 1
        count1 = 0
        
    if count2 >= 10:
        face_count2 += 1
        count2 = 0
    
    cv2.putText(frame1, "Autos: " + str(face_count1), (10, 30), font_face, font_scale, text_color, font_thickness)
    cv2.putText(frame2, "Autos: " + str(face_count2), (10, 30), font_face, font_scale, text_color, font_thickness)
    
    if face_count1 > face_count2:
        text = "Tiene Paso"
        text_size, _ = cv2.getTextSize(text, font_face, font_scale, font_thickness)
        text_x = int((frame1.shape[1] - text_size[0]) / 2)
        text_y = int((frame1.shape[0] + text_size[1]) / 2)
        cv2.putText(frame1, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 255), font_thickness)
    elif face_count2 > face_count1:
        text = "Tiene Paso"
        text_size, _ = cv2.getTextSize(text, font_face, font_scale, font_thickness)
        text_x = int((frame2.shape[1] - text_size[0]) / 2)
        text_y = int((frame2.shape[0] + text_size[1]) / 2)
        cv2.putText(frame2, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 255), font_thickness)
    
    if (face_count1 + face_count2) > 200:
        text = "Umbral superado"
        text_size, _ = cv2.getTextSize(text, font_face, font_scale, font_thickness)
        text_x = int((frame1.shape[1] - text_size[0]) / 2)
        text_y = int((frame1.shape[0] + text_size[1]) / 2)
        cv2.putText(frame1, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 255), font_thickness)

    cv2.imshow('frame1', frame1)
    cv2.imshow('frame2', frame2)
   
   

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows
