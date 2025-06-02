import imageio.v3 as iio
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
from scipy.signal import convolve
import os

#image = iio.imread(uri="IR_900-Tur_6000-W_0.png")#"IR_900-Tur_4500-W_0.png"
Bees = iio.imread(uri="Vcely.png")
Varroa = iio.imread(uri="Kliestiky.png")#, mode="L")

colors = ("red", "green", "blue")
Kernel = [0.25,0.5,0.25]

address="C:\\Users\\Samuel\\OneDrive - VUT\\VUT_Brno_FEKT\\DP\\FotoRoznePomeryOsvetleni\\CameraLog"
dir_list = os.listdir(address)
#print(dir_list)
Maximum=-1
MaxName=""
a=0

maskB = Bees>0
maskV = Varroa>0


for name in dir_list:
    print(a)
    a+=1
    image = iio.imread(uri=address+"\\"+name)
    #Bees
    HistogramBee = np.zeros([256,3])
    Bees=np.zeros([258,3])
    for (channel_id, color) in enumerate(colors):
        for i in range (maskB.shape[0]):
            for j in range (maskB.shape[1]):
                if(maskB[i,j]==True):
                    HistogramBee[image[i,j,channel_id],channel_id]+=1
        Bees[:,channel_id] = convolve(HistogramBee[:,channel_id],Kernel)
        Bees[:,channel_id] = Bees[:,channel_id]/Bees[:,channel_id].sum()


    #Varroa Destructor
    HistogramVarroa = np.zeros([256,3])
    Varroas=np.zeros([258,3])
    for (channel_id, color) in enumerate(colors):
        for i in range (maskV.shape[0]):
            for j in range (maskV.shape[1]):
                if(maskV[i,j]==True):
                    HistogramVarroa[image[i,j,channel_id],channel_id]+=1
        Varroas[:,channel_id] = convolve(HistogramVarroa[:,channel_id],Kernel)
        Varroas[:,channel_id] = Varroas[:,channel_id]/Varroas[:,channel_id].sum()


    #Background
    HistogramBackground = np.zeros([256,3])
    Backgrounds=np.zeros([258,3])
    for channel_id, color in enumerate(colors):
        for i in range (maskV.shape[0]):
            for j in range (maskV.shape[1]):
                if(maskV[i,j]==False and maskB[i,j]==False):
                    HistogramBackground[image[i,j,channel_id],channel_id]+=1
        Backgrounds[:,channel_id] = convolve(HistogramBackground[:,channel_id],Kernel)
        Backgrounds[:,channel_id]=Backgrounds[:,channel_id]/Backgrounds[:,channel_id].sum()

    PearsonBB = 0
    PearsonBV = 0
    PearsonVB = 0
    for i in range(3):
        PearsonBB += (1-abs(scipy.stats.pearsonr(Backgrounds[:,i], Bees[:,i])[0]))
        PearsonBV += (1-abs(scipy.stats.pearsonr(Bees[:,i], Varroas[:,i])[0]))
        PearsonVB += (1-abs(scipy.stats.pearsonr(Varroas[:,i], Backgrounds[:,i])[0]))
    # print(PearsonBB)
    # print(PearsonBV)
    # print(PearsonVB)

    #Geometric mean
    GM=scipy.stats.mstats.gmean([PearsonBB,PearsonBV,PearsonVB])
    if GM>Maximum:
        Maximum=GM
        MaxName=name
        print(Maximum)
        print(MaxName)
    # print(GM)

print(Maximum)
print(MaxName)