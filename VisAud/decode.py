import numpy as np
import cv2
import soundfile as sf

data, samplerate = sf.read('A.wav')
refData = (255)*data
print (refData)
threeD = refData.reshape((3, 800, 600)).transpose()
# 3,9,9
print("----------3D Refactor--------------")
print(threeD)
#gray = cv2.cvtColor(threeD, cv2.COLOR_BGR2GRAY)
cv2.imshow('image',threeD)
cv2.waitKey(0)
cv2.destroyAllWindows()
