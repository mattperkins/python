import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

print(digits.data)
print(digits.target)
print(digits.images[0])

    # gamma defines the fine grain of 'gradient descent' // e.g the learning rate  
clf = svm.SVC(gamma=0.0001, C=100)

print(len(digits.data))

    # training dataset
x,y = digits.data[:-10], digits.target[:-10]
clf.fit(x,y)

print('Prediction:',clf.predict(digits.data[[-5]]))

plt.imshow(digits.images[-5], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()