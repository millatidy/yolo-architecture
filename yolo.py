from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.layers import LeakyReLU

length =  448
width = 448

input_shape = (length, width, 3)

LeakyRelu = LeakyReLU(alpha=0.1)

model = Sequential()
model.add(Conv2D(filters=64, kernel_size=(7,7), input_shape=input_shape, activation=LeakyRelu, strides=(1, 1)))
model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

model.add(Conv2D(filters=192, kernel_size=(3,3), activation=LeakyRelu))
model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

model.add(Conv2D(filters=128, kernel_size=(1,1), activation=LeakyRelu))
model.add(Conv2D(filters=256, kernel_size=(3,3), activation=LeakyRelu))
model.add(Conv2D(filters=256, kernel_size=(1,1), activation=LeakyRelu))
model.add(Conv2D(filters=512, kernel_size=(3,3), activation=LeakyRelu))
model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

for i in range(4):
	model.add(Conv2D(filters=256, kernel_size=(1,1), activation=LeakyRelu))
	model.add(Conv2D(filters=512, kernel_size=(3,3), activation=LeakyRelu))
model.add(Conv2D(filters=512, kernel_size=(3,3), activation=LeakyRelu))
model.add(Conv2D(filters=1024, kernel_size=(3,3), activation=LeakyRelu))
model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

for i in range(2):
	model.add(Conv2D(filters=512, kernel_size=(1,1), activation=LeakyRelu))
	model.add(Conv2D(filters=1024, kernel_size=(3,3), activation=LeakyRelu))
model.add(Conv2D(filters=1024, kernel_size=(3,3), activation=LeakyRelu))
model.add(Conv2D(filters=1024, kernel_size=(3,3), strides=(2,2), activation=LeakyRelu))

model.add(Conv2D(filters=1024, kernel_size=(3,3), activation=LeakyRelu))
model.add(Conv2D(filters=1024, kernel_size=(3,3), activation=LeakyRelu))

model.add(Flatten())
model.add(Dense(units=(1024), activation=LeakyRelu))
model.add(Dense(units=(1470), activation='relu'))

print (model.summary())
