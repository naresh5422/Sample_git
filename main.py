import cv2
import os
import pickle
import numpy as np
import face_recognition
cap = cv2.VideoCapture(0)
#cap.set(3, 160) # Width
#cap.set(4, 110) # Height
cap.set(3, 650)
cap.set(4, 440)
img_bgr = cv2.imread('AccentureCC.png')

# Load the encoding file here
print("Loaded encode file....!")
file = open("EncodeFile.p", "rb")
encodeListKnownIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownIds
#print(studentIds)
print("Encode file is loaded..!")

while True:
    f, img = cap.read()
    img_size = cv2.resize(img, (0,0), None, 0.25, 0.25)
    bgr_img = cv2.cvtColor(img_size, cv2.COLOR_BGR2RGB)
    curFaceFrames = face_recognition.face_locations(bgr_img)
    curFaceEncode = face_recognition.face_encodings(bgr_img, curFaceFrames)
    #img_bgr[108:108+120, 950: 950+160] = img
    #print(img_size)
    #print(bgr_img)
    print(curFaceFrames)
    print(curFaceEncode)
#    for faceEnco, faceLoc in zip(curFaceEncode, curFaceFrames):
        # Lower the distance better the match
 #       matches = face_recognition.compare_faces(encodeListKnown, faceEnco)
#        faceDist = face_recognition.face_distance(encodeListKnown, faceEnco)  
#        print(matches)
#        print(faceDist)
 #       matchIndex = np.argmin(faceDist)
#        print("Match index", matchIndex)
        
#        if matches[matchIndex]:
#            print('known face detected')
#        else:
#            print("No face is there")
        
    cv2.imshow("Display the Camera", img)
    #cv2.imshow("BackGound", img_bgr)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
    
   
cap.release()
cv2.destroyAllWindows()