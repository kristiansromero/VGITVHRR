import numpy as np
import cv2
import soundfile as sf
from soundfile import SoundFile

frequency = 2100000000
channels = 1
filename = 'A.wav'
img = cv2.imread('desert.jpg')
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img = gray
print (img)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3D array is flattened to a 1D array
print ("--------Flattened-------")
flatIm = img.flatten('F')
print (flatIm)
#Scaled to be able to be written onto soundfile
print ("--------Scaled----------")
flatIm = flatIm/255.0
print (flatIm)
#print ("--------Unscale---------")
#flatIm = 255**flatIm
#print(flatIm)

with SoundFile('A.wav', 'w', frequency, channels, 'PCM_24') as f:
    f.write(flatIm);
