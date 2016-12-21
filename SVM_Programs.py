# Support Vector Machines with Python

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
print('Prediction: ', clf.predict(digits.data[-1])) # prediction done here

plt.imshow(digits.images[-1], cmap = plt.cm.gray_r, interpolation = "nearest")
# imshow = shows images, 'cmap' is just blowing up the image to a larger size

plt.show()

'''
x, y = digits.data[:-10], digits.target[:-10]

clf.fit(x, y)
print('Prediction: ', clf.predict(digits.data[-4])))  # prediction done here

plt.imshow(digits.images[-4], cmap = plt.cm.gray_r, interpolation="nearest")  
plt.show()
'''

# change gamma = 0.001 to gamma = 0.01 and check out the changes
