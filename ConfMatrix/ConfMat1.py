import matplotlib.pyplot as plt
import numpy
from sklearn import metrics

confusion_matrix = numpy.array([[1893, 588],[207,0]])#Vsetky obrazky..."Tabuľka klasifikácií (Confusion matrix) všetkých obrázkov"
confusion_matrix = numpy.array([[954, 513],[204,0]])#Obrazky bez kliestikov..."Tabuľka klasifikácií (Confusion matrix) bez samotných klieštikov"
confusion_matrix = numpy.array([[806, 661],[10,0]])#Obrazky bez kliestikov..."Tabuľka klasifikácií (Confusion matrix) bez klieštikov menších ako 20 pxl"
# # confusion_matrix = numpy.array([[2431, 50],[280,0]])#Obrazky bez kliestikov..."Tabuľka klasifikácií (Confusion matrix) modelu s upravenou chybovou funkciou"
confusion_matrix = numpy.array([[1417, 50],[277,0]])#Obrazky bez kliestikov..."Tabuľka klasifikácií (Confusion matrix) modelu s upravenou chybovou funkciou bez samotných klieštikov"
confusion_matrix = numpy.array([[2223, 258],[204,0]])#Obrazky bez kliestikov..."Tabuľka klasifikácií (Confusion matrix)\nmodelu po 90 epochách"
confusion_matrix = numpy.array([[1219, 248],[186,0]])#Obrazky bez kliestikov..."Tabuľka klasifikácií (Confusion matrix) modelu\npo 90 epochách bez samotných klieštikov"
#confusion_matrix = numpy.array([[2422, 59],[158,0]])#Obrazky bez kliestikov..."Tabuľka klasifikácií (Confusion matrix)\nmodelu po 130 epochách"
confusion_matrix = numpy.array([[1409, 58],[142,0]])#Obrazky bez kliestikov..."Tabuľka klasifikácií (Confusion matrix) modelu\npo 90 epochách bez samotných klieštikov"
#confusion_matrix = numpy.array([[19, 8],[47,0]])#Obrazky bez kliestikov..."Tabuľka klasifikácií (Confusion matrix) bez klieštikov menších ako 20 pxl"
#confusion_matrix = numpy.array([[315, 1152],[1323,0]])#Obrazky bez kliestikov..."Tabuľka klasifikácií (Confusion matrix) bez klieštikov menších ako 20 pxl"
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = ["Klieštik", "Bez klieštika"])
# cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = ["With Varroa", "Without Varroa"])

plt.rcParams.update({'font.size': 16})
cm_display.plot(colorbar=False, cmap="Blues", text_kw = {"size": 48})
#plt.rcParams.update({'font.size': 8})
plt.title("Tabuľka klasifikácií (Confusion matrix) modelu\npo 130 epochách bez samotných klieštikov")
#plt.rcParams.update({'font.size': 8})
plt.xlabel("Predikcie")
# plt.xlabel("Predictions")
#plt.rcParams.update({'font.size': 8})
plt.ylabel("Skutočnosť")
# plt.ylabel("Ground truth")

plt.show()


