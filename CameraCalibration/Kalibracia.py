import numpy as np
import cv2 as cv
import glob
import os 

fx = 28511
fy = 29826
cx = 634.6212
cy = 362.5117

k1 = -248.572842168091
k2 = 63489.7810239253

mtx = np.zeros((3,3))
mtx[0,0] = fx
mtx[1,1] = fy
mtx[0,2] = cx
mtx[1,2] = cy
mtx[2,2] = 1

dist = np.zeros(4)
dist[0] = k1
dist[1] = k2

# Get the list of all files and directories
ReadPath = "C:\\Users\\Samuel\\Desktop\\Vcely s kliestikom pred liecenim\\CameraLog\\IR"
dir_list = os.listdir(ReadPath)
print("Files and directories in '", ReadPath, "' :")
# prints all files
#print(dir_list)

WritePath = "C:\\Users\\Samuel\\Desktop\\Vcely s kliestikom pred liecenim\\CameraLog\\IR\\PoKalibraci\\"
for path in dir_list:
    if path != 'PoKalibraci':
        RP = ReadPath + '\\' + path
        #print(RP)
        img = cv.imread(RP)
        h,  w = img.shape[:2]


        newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
        # undistort
        dst = cv.undistort(img, mtx, dist, None, newcameramtx)
        #dst = cv.undistort(img, mtx, dist, None)
        
        # crop the image
        x, y, w, h = roi
        dst = dst[y:y+h, x:x+w]#cropnutie po kalibracii (aby tam neboli tie cierne one pri hranach)
        crop = dst[164:464,49:1165]
        #print(dst.shape)
        #cv.imshow('Img2',dst)
        cv.imwrite(WritePath+path, crop)
        print(WritePath+path)
        # cv.waitKey(0)
        # cv.destroyAllWindows()
print("The end")




# Importing Image class from PIL module
# from PIL import Image
# im = Image.open("W_kal.png")

# left = 12
# top = 162
# right = 1188
# bottom =462

# im1 = im.crop((left, top, right, bottom))
 
# # Shows the image in image viewer
# im1.save('W_crop.png')

# from PIL import Image
# image1 = Image.open("W_crop.png")
# image2 = Image.open("IR_crop.png")
# image3 = Image.open("Tur_crop.png")


# image1_size = image1.size
# image2_size = image2.size
# new_image = Image.new("RGB",(image1_size[0], 3*image1_size[1]), (250,250,250))
# new_image.paste(image1,(0,0))
# new_image.paste(image3,(0,image1_size[1]))
# new_image.paste(image2,(0,2*image1_size[1]))
# new_image.save("Spojene.png")
# new_image.show()