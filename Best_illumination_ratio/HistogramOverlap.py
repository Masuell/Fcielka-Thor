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


for name in dir_list:
    print(a)
    a+=1
    image = iio.imread(uri=address+"\\"+name)
    #Bees
    HistogramBee = np.zeros([256,3])
    Bees=np.zeros([260,3])
    for (channel_id, color) in enumerate(colors):
        for i in range (maskB.shape[0]):
            for j in range (maskB.shape[1]):
                if(maskB[i,j]==True):
                    HistogramBee[image[i,j,channel_id],channel_id]+=1
        Bees[:,channel_id] = convolve(convolve(HistogramBee[:,channel_id],Kernel),Kernel)
        Bees[:,channel_id] = Bees[:,channel_id]/(Bees[:,channel_id].sum())

    #Varroa Destructor
    HistogramVarroa = np.zeros([256,3])
    Varroas=np.zeros([260,3])
    for (channel_id, color) in enumerate(colors):
        for i in range (maskV.shape[0]):
            for j in range (maskV.shape[1]):
                if(maskV[i,j]==True):
                    HistogramVarroa[image[i,j,channel_id],channel_id]+=1
        Varroas[:,channel_id] = convolve(convolve(HistogramVarroa[:,channel_id],Kernel),Kernel)
        Varroas[:,channel_id] = Varroas[:,channel_id]/(Varroas[:,channel_id].sum())


    #Background
    HistogramBackground = np.zeros([256,3])
    Backgrounds=np.zeros([260,3])
    for channel_id, color in enumerate(colors):
        for i in range (maskV.shape[0]):
            for j in range (maskV.shape[1]):
                if(maskV[i,j]==False and maskB[i,j]==False):
                    HistogramBackground[image[i,j,channel_id],channel_id]+=1
        Backgrounds[:,channel_id] = convolve(convolve(HistogramBackground[:,channel_id],Kernel),Kernel)
        Backgrounds[:,channel_id]=Backgrounds[:,channel_id]/(Backgrounds[:,channel_id].sum())

    OverlapBB = 0
    OverlapBV = 0
    OverlapVB = 0
    for j in range(Backgrounds.shape[1]):
        for i in range(Backgrounds.shape[0]):
            OverlapBB += min(Backgrounds[i,j],Bees[i,j])
            OverlapBV += min(Bees[i,j],Varroas[i,j])
            OverlapVB += min(Varroas[i,j],Backgrounds[i,j])
    # print(PearsonBB)
    # print(PearsonBV)
    # print(PearsonVB)

    #Geometric mean
    GM=scipy.stats.mstats.gmean([1/OverlapBB,1/OverlapBV,1/OverlapVB])
    #GM = OverlapBB+OverlapBV+OverlapVB
    if GM>Maximum:
        Maximum=GM
        MaxName=name
        print("Nove Max")
        print(Maximum)
        print(MaxName)
    if GM<Minimum:
        Minimum=GM
        MinName=name
        print("Nove Min:")
        print(Minimum)
        print(MinName)
    #print(GM)
print("Koniec programu:")
print(Maximum)
print(MaxName)
print(Minimum)
print(MinName)



# print(a)
# a+=1
# image = iio.imread(uri="Bhattacharyya_1_76_IR_2100-Tur_6000.png")
# #Bees
# HistogramBee = np.zeros([256,3])
# Bees=np.zeros([260,3])
# for (channel_id, color) in enumerate(colors):
#     for i in range (maskB.shape[0]):
#         for j in range (maskB.shape[1]):
#             if(maskB[i,j]==True):
#                 HistogramBee[image[i,j,channel_id],channel_id]+=1
#     Bees[:,channel_id] = convolve(convolve(HistogramBee[:,channel_id],Kernel),Kernel)
#     Bees[:,channel_id] = Bees[:,channel_id]/(Bees[:,channel_id].sum())

# #Varroa Destructor
# HistogramVarroa = np.zeros([256,3])
# Varroas=np.zeros([260,3])
# for (channel_id, color) in enumerate(colors):
#     for i in range (maskV.shape[0]):
#         for j in range (maskV.shape[1]):
#             if(maskV[i,j]==True):
#                 HistogramVarroa[image[i,j,channel_id],channel_id]+=1
#     Varroas[:,channel_id] = convolve(convolve(HistogramVarroa[:,channel_id],Kernel),Kernel)
#     Varroas[:,channel_id] = Varroas[:,channel_id]/(Varroas[:,channel_id].sum())


# #Background
# HistogramBackground = np.zeros([256,3])
# Backgrounds=np.zeros([260,3])
# for channel_id, color in enumerate(colors):
#     for i in range (maskV.shape[0]):
#         for j in range (maskV.shape[1]):
#             if(maskV[i,j]==False and maskB[i,j]==False):
#                 HistogramBackground[image[i,j,channel_id],channel_id]+=1
#     Backgrounds[:,channel_id] = convolve(convolve(HistogramBackground[:,channel_id],Kernel),Kernel)
#     Backgrounds[:,channel_id]=Backgrounds[:,channel_id]/(Backgrounds[:,channel_id].sum())

# OverlapBB = 0
# OverlapBV = 0
# OverlapVB = 0
# for j in range(Backgrounds.shape[1]):
#     for i in range(Backgrounds.shape[0]):
#         OverlapBB += min(Backgrounds[i,j],Bees[i,j])
#         OverlapBV += min(Bees[i,j],Varroas[i,j])
#         OverlapVB += min(Varroas[i,j],Backgrounds[i,j])
# # print(PearsonBB)
# # print(PearsonBV)
# # print(PearsonVB)

# #Geometric mean
# GM=scipy.stats.mstats.gmean([OverlapBB,OverlapBV,OverlapVB])
# if GM>Maximum:
#     Maximum=GM
#     #MaxName=name
#     print(Maximum)
#     #print(MaxName)
