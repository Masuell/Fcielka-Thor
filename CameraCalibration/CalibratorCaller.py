from Calibrator import Calibrator
import cv2 as cv

ReadPath = "C:\\Users\\Samuel\\OneDrive - VUT\\VUT_Brno_FEKT\\DP\\Kalibracia\\Kalib1\\241124_161252159883.png"
Cal = Calibrator()
img = cv.imread(ReadPath)
ImgCal = Cal.Calib(img)
cv.imshow('Img',ImgCal)
cv.waitKey(0)
cv.destroyAllWindows()