import imageio.v3 as iio
import ipympl
import matplotlib.pyplot as plt
import numpy as np
import skimage as ski
from scipy.signal import convolve

image = iio.imread(uri="Prekrytie_1_103_IR_5400-Tur_16500.png")#"IR_900-Tur_4500-W_0.png"
Bees = iio.imread(uri="Vcely.png")
Varroa = iio.imread(uri="Kliestiky.png")#, mode="L")

Kernel = [0,1,0]
Kernel2 = [0.25,0.5,0.25]
Kernel3 = np.array([1,1,1])/3
Kernel4 = [0.4,0.2,0.4]

colors = ("red", "green", "blue")

# create the histogram plot, with three lines, one for
# each color
fig, ax = plt.subplots()
ax.set_xlim([0, 258])
for channel_id, color in enumerate(colors):
    histogram, bin_edges = np.histogram(
        image[:, :, channel_id], bins=256, range=(0, 256)
    )
    # print(type(histogram))
    # print(histogram.shape)
    histogram=convolve(histogram,Kernel)
    histogram = histogram/histogram.sum()
    #ax.plot(bin_edges[0:-1], histogram, color=color)
    ax.plot(histogram, color=color)
ax.set_title("Histogram celeho obrazku")
ax.set_xlabel("Color value")
ax.set_ylabel("Pixel count")

#print(Bees)
mask = np.zeros(shape=Bees.shape[0:2], dtype="bool")
mask = Bees>0



# just for display:
# make a copy of the image, call it masked_image, and
# zero values where mask is False


# create a new figure and display masked_img, to verify the
# validity of your mask
# fig, ax = plt.subplots()
# ax.set_title("Maska vcely")
# ax.imshow(mask, cmap="gray")


# create the histogram plot, with three lines, one for
# each color
fig, ax = plt.subplots()
ax.set_xlim([0, 258])

histogram = np.zeros([256])


for (channel_id, color) in enumerate(colors):
    histogram = np.zeros([256])
    for i in range (mask.shape[0]):
        for j in range (mask.shape[1]):
            if(mask[i,j]==True):
                histogram[image[i,j,channel_id]]+=1
    # print(type(histogram))
    # print(histogram.shape)
    histogram1=convolve(histogram,Kernel)
    histogram1 = histogram1/histogram1.sum()
    # histogram2=convolve(histogram,Kernel3)
    # histogram3=convolve(histogram,Kernel3)
    ax.plot(histogram1, color=color)
    # ax.plot(histogram2, color=color)
    # ax.plot(histogram3, color=color)
ax.set_title("Histogram vceliciek")
ax.set_xlabel("Bee color value")
ax.set_ylabel("Bee pixel count")


fig, ax = plt.subplots()
ax.set_xlim([0, 258])
# ax.imshow(mask, cmap="gray")
mask = Varroa>0




for (channel_id, color) in enumerate(colors):
    histogram = np.zeros([256])
    for i in range (mask.shape[0]):
        for j in range (mask.shape[1]):
            if(mask[i,j]==True):
                histogram[image[i,j,channel_id]]+=1
    histogram1=convolve(histogram,Kernel)
    histogram1 = histogram1/histogram1.sum()
    # histogram2=convolve(histogram,Kernel3)
    # histogram3=convolve(histogram2,Kernel3)
    ax.plot(histogram1, color=color)
    #ax.plot(histogram2, color=color)
    #ax.plot(histogram3, color=color)
    # print(histogram3.shape)
    # x=np.arange(0,260,1)
    # print(x.shape)
    # ax.scatter(x,histogram3, color=color)
ax.set_title("Histogram kliestikov")
ax.set_xlabel("Varroa color value")
ax.set_ylabel("Varroa pixel count")


# fig, ax = plt.subplots()
# ax.set_title("Maska kliestika")
# ax.imshow(mask, cmap="gray")

plt.show()