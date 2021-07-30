import cv2
import numpy as np
from skimage import io
 
img = cv2.imread("Golden-Retriever.jpg")


while True: 
    cv2.imshow("img",img)
    
    #Converting to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow("imageRGB",img)
    
    #Detecting edges of the input image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    cv2.imshow("edges",edges)
    
    #Cartoonifying the image
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    cv2.imshow("Cartoon",cartoon)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()