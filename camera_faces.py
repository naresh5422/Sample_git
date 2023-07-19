# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 22:33:50 2023

@author: nares
"""

import os
import cv2

cap = cv2.VideoCapture(0)
#cap.set(3, 1280)
#cap.set(4, 750)


while True:
    f, img = cap.read()
    cv2.imshow("Video by camera", img)
    if cv2.waitKey(0) & 0XFF == ord('q'):
        break