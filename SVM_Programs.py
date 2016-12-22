# Support Vector Machines with Python

# Basic Outline:

import numpy
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import datasets

# Assume that you have, x (predictor) and y (target) for training data set and x_test(predictor) of test_dataset

clf = svm.SVC(kernel = "linear", C = 1, gamma = 1)
# Create SVM classification object, C = SVM Regularization Parameter

# Next, train the model using training sets and check score
clf.fit(x, y)
clf.score(x, y)

prediction = clf.predict(x_test)

# Program - 01: Image Recognition

import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import datasets
# scikit-learn already has training data-sets

digits = datasets.load_digits()

# print(digits.data)
# print(digits.target)
# print(digits.images[0])
# print(len(digits.data))

clf = svm.SVC(gamma = 0.001, C = 100)
# clf = classifier, gamma = α (gradient-descent)

x, y = digits.data[:-1], digits.target[:-1]
# training data-set is set up, with data-set (from start till end ([:-1]))

clf.fit(x, y) # fits a line through the data-set
print('Prediction: ', clf.predict(digits.data[-1])) 
# prediction for last element is done here

plt.imshow(digits.images[-1], cmap = plt.cm.gray_r, interpolation = "nearest")
# imshow = shows images, 'cmap' is just blowing up the image to a larger size

plt.show()

'''
x, y = digits.data[:-10], digits.target[:-10]

clf.fit(x, y)
print('Prediction: ', clf.predict(digits.data[-4]))  # prediction done here

plt.imshow(digits.images[-4], cmap = plt.cm.gray_r, interpolation="nearest")  
plt.show()
'''

# change gamma = 0.001 to gamma = 0.01 and check out the changes

# Program - 02:

import numpy
import matplotlib.pyplot as plt
from sklearn import svm, datasets

iris = datasets.load_iris() # load some data for manipulation
x = iris.data[:, :2] # we take only first two features
y = iris.target

clf = svm.SVC(kernel = "linear", C = 1, gamma = 0).fit(x, y)

# create a mesh to plot
x_min, x_max = x[:, 0]. min() - 1, x[:, 0].max() + 1
y_min, y_max = y[:, 0]. min() - 1, y[:, 0].max() + 1
h = (x_max / x_min) / 100
xx, yy = numpy.meshgrid(np.arrange(x_min, x_max, h), np.arrange(y_min, y_max, h))

plt.subplot(1, 1, 1)

Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)

plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.title('SVC with linear kernel')
plt.show()

# Reference: http://scikit-learn.org/stable/tutorial/basic/tutorial.html
