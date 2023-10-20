import matplotlib.pyplot as plt
import numpy
from sklearn import metrics

actual = numpy.random.binomial(1,.9,size = 1000)
print(actual)
predicted = numpy.random.binomial(1,.9,size = 1000)
print(predicted)
confusion_matrix = metrics.confusion_matrix(actual, predicted)
print(confusion_matrix)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])
print(cm_display)
cm_display.plot()
plt.show()