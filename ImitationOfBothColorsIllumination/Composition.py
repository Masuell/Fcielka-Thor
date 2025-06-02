# import opencv
import cv2
import numpy as np
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os

IRdir = "C:\\Users\\Samuel\\OneDrive - VUT\\VUT_Brno_FEKT\\DP\\Skladanie_obrazkov\\TestDS\\IR\\"
IR = os.listdir(IRdir)
Turdir="C:\\Users\\Samuel\\OneDrive - VUT\\VUT_Brno_FEKT\\DP\\Skladanie_obrazkov\\TestDS\\Tur\\"
Tur = os.listdir(Turdir)


# print(IRdir + IR[1])
Image = np.zeros([300,1116,3])
for i in range(len(IR)):
    # print(i)
    # print(IR)
    # print(IRdir + str(IR[i]))
    ImageIR = cv2.imread(IRdir + str(IR[i]))
    ImageTur = cv2.imread(Turdir + str(Tur[i]))
    Image[:,:,2] = (ImageIR[:,:,2]*1.9015503+ImageTur[:,:,2]*0.11981642-239.3958689153346)
    Image[:,:,1] = (ImageIR[:,:,1]*0.22510276+ImageTur[:,:,1]*0.76001174-13.914223532598015)
    Image[:,:,0] = (ImageIR[:,:,0]*0.49195204+ImageTur[:,:,0]*0.56534815-11.093601483354604)
    cv2.imwrite("C:\\Users\\Samuel\\OneDrive - VUT\\VUT_Brno_FEKT\\DP\\Skladanie_obrazkov\\TestDS\\Vysledok\\"+str(IR[i]+".png"),Image)

cv2.waitKey()
