# Fcielka-Thor

This repository contains programms which were used for diploma thesis about [Varroa Destructor detection on honey bees with using narrow spectra of illumination](https://www.vut.cz/studenti/zav-prace/detail/167591).

The thesis focuses on the development of a system for detecting mites on bees using computer vision techniques and illumination with specific wavelengths. The wavelengths employed are 500 nm, corresponding to turquoise light, and 780 nm, corresponding to infrared light. Both classical image processing methods and deep learning approaches are utilized. The primary objective was to capture images of bees as they pass through a [Bee Health Monitor device](https://github.com/boortel/Bee-Health-Monitor) while being illuminated with a narrow spectrum of light. Another goal was to train models capable of reliably identifying mites on bees, thereby reducing the need for manual hive inspections. The developed models include the YOLOv11 object detection architecture and the U-net semantic segmentation architecture, both of which achieved satisfactory performance. A key remaining challenge is the accurate detection of mites located on the edges of bees, which may be addressed by simultaneous illumination with both wavelengths.

You can find [the created dataset here](https://www.kaggle.com/datasets/masuel/bee-hyperspectral-dataset). It consists of photos of bees, mites and bees with mites before and after fumigation treatment. All categories is illuminated by IR, turquoise or white light. Besides that, there is also annotation for semantic segmentation (1 color channel = 1 category) and object detector (YOLO format) there. 

In Best_illumination_ratio folder is code to determine the best illumination ratio (if both colors are turned on).

In CameraCalibration folder is Calibrator module for Bee Health Monitor device.

ImitationOfBothColorsIllumination folder is code to simulate photos with both illumination. The pictures are composed of photos under IR and turquoise with linear regression.

As detection models were used [U-net semantic segmentation architecture](https://github.com/milesial/Pytorch-UNet) and [YOLOv11](https://github.com/ultralytics/ultralytics) object detection architecture. 
