from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D

length =  448
width = 448

input_shape = (length, width)

model = Sequential()
model.add(Conv2D(filters=64, kernel_size=(7,7), input_shape=input_shape, activation='relu', strides=(1, 1)))
model.add(MaxPooling2D(pool_size(2,2), strides=(2,2)))

model.add(Conv2D(filters=192, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

model.add(Conv2D(filters=128, kernel_size=(1,1), activation='relu'))
model.add(Conv2D(filters=256, kernel_size=(3,3), activation='relu'))
model.add(Conv2D(filters=256, kernel_size=(1,1), activation='relu'))
model.add(Conv2D(filters=512, kernel_size=(3,3), activation='relu'))
modle.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

for i in range(4):
	model.add(Conv2D(filters=256, kernel_size=(1,1), activation='relu'))
	model.add(Conv2D(filters=512, kernel_size=(3,3), activation='relu'))
model.add(Conv2D(filters=512, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

for i in range(2):
	model.add(Conv2D(filters=512, kernel_size=(1,1), activation='relu'))
	model.add(Conv2D(filters=1024, kernel_size=(3,3), activation='relu'))
model.add(Conv2D(filters=1024, kernel_size=(3,3), activation='relu'))
model.add(Conv2D(filters=1024, kernel_size=(3,3), strides=(2,2), activation='relu'))

model.add(Conv2D(filters=1024, kernel_size=(3,3), activation='relu'))
model.add(Conv2D(filters=1024, kernel_size=(3,3), activation='relu'))