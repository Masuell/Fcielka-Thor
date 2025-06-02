import imageio.v3 as iio
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
from scipy.signal import convolve
from sklearn.metrics.pairwise import cosine_similarity
import os
import cv2

#image = iio.imread(uri="IR_900-Tur_6000-W_0.png")#"IR_900-Tur_4500-W_0.png"
Bees = iio.imread(uri="Vcely.png")
Varroa = iio.imread(uri="Kliestiky.png")#, mode="L")

colors = ("red", "green", "blue")
Kernel = np.array([1,1,1])/3

address="C:\\Users\\Samuel\\OneDrive - VUT\\VUT_Brno_FEKT\\DP\\FotoRoznePomeryOsvetleni\\CameraLog"
dir_list = os.listdir(address)
#print(dir_list)
Maximum=-1
MaxName=""
Minimum=300
MinName=""
a=0

maskB = Bees>0
maskV = Varroa>0
print(maskV)
maskBackground = np.zeros((300,1116),dtype='bool')
maskBackground = np.bitwise_and(np.invert(maskB), np.invert(maskV))
cv2.imshow('sdfgh', 255*maskBackground.astype('uint8'))
cv2.waitKey()
cv2.destroyAllWindows()

for name in dir_list:
    print(a)
    a+=1
    image = iio.imread(uri=address+"\\"+name)
    #Bees
    HistogramBee = np.zeros([256,3])
    Bees=np.zeros([260,3])
    for (channel_id, color) in enumerate(colors):
        channel_data = image[:, :, channel_id][maskB] #b je maska
        HistogramBee[:,channel_id], bin_edges = np.histogram(channel_data, bins=256, range=(0, 256))
        # for i in range (maskB.shape[0]):
        #     for j in range (maskB.shape[1]):
        #         if(maskB[i,j]==True):
                    # HistogramBee[image[i,j,channel_id],channel_id]+=1
        Bees[:,channel_id] = convolve(convolve(HistogramBee[:,channel_id],Kernel),Kernel)
        Bees[:,channel_id] = Bees[:,channel_id]/(Bees[:,channel_id].sum())

    #Varroa Destructor
    HistogramVarroa = np.zeros([256,3])
    Varroas=np.zeros([260,3])
    for (channel_id, color) in enumerate(colors):
        channel_data = image[:, :, channel_id][maskV] #b je maska
        HistogramVarroa[:,channel_id], bin_edges = np.histogram(channel_data, bins=256, range=(0, 256))
        # for i in range (maskV.shape[0]):
        #     for j in range (maskV.shape[1]):
        #         if(maskV[i,j]==True):
        #             HistogramVarroa[image[i,j,channel_id],channel_id]+=1
        Varroas[:,channel_id] = convolve(convolve(HistogramVarroa[:,channel_id],Kernel),Kernel)
        Varroas[:,channel_id] = Varroas[:,channel_id]/(Varroas[:,channel_id].sum())


    #Background
    HistogramBackground = np.zeros([256,3])
    Backgrounds=np.zeros([260,3])
    for channel_id, color in enumerate(colors):
        channel_data = image[:, :, channel_id][maskBackground] #b je maska
        HistogramBackground[:,channel_id], bin_edges = np.histogram(channel_data, bins=256, range=(0, 256))
        # for i in range (maskV.shape[0]):
        #     for j in range (maskV.shape[1]):
        #         if(maskV[i,j]==False and maskB[i,j]==False):
        #             HistogramBackground[image[i,j,channel_id],channel_id]+=1
        Backgrounds[:,channel_id] = convolve(convolve(HistogramBackground[:,channel_id],Kernel),Kernel)
        Backgrounds[:,channel_id]=Backgrounds[:,channel_id]/(Backgrounds[:,channel_id].sum())

    CDBB = 0
    CDBV = 0
    CDVB = 0
    for i in range(3):
        CDBB += 1-cosine_similarity(Backgrounds.reshape(1, -1), Bees.reshape(1, -1))[0, 0]
        CDBV += 1-cosine_similarity(Bees.reshape(1, -1), Varroas.reshape(1, -1))[0, 0]
        CDVB += 1-cosine_similarity(Varroas.reshape(1, -1), Bees.reshape(1, -1))[0, 0]
    # print(PearsonBB)
    # print(PearsonBV)
    # print(PearsonVB)

    #Geometric mean
    GM=scipy.stats.mstats.gmean([CDBB,CDBV,CDVB])
    if GM>Maximum:
        Maximum=GM
        MaxName=name
        print(Maximum)
        print(MaxName)
    if GM<Minimum:
        Minimum=GM
        MinName=name
        print(Minimum)
        print(MinName)
    #print(GM)
print("Koniec programu:Max:")
print(Maximum)
print(MaxName)
print("Min:")
print(Minimum)
print(MinName)
#         channel_data = ScaledImage[:, :, i][b] #b je maska
#         histogram, bin_edges = np.histogram(channel_data, bins=256, range=(0, 256))