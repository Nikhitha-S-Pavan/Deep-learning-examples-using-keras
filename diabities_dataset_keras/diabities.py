from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense, Dropout

# load the dataset
dataset = loadtxt('C:\\Users\\NIU2KOR\\Desktop\\learning\\machine_learning\\diabities.csv', delimiter=',')
print(dataset.shape)
# split into input (X) and output (y) variables
X = dataset[:, 0:8]
y = dataset[:, 8]



# define the keras model
model = Sequential()
model.add(Dense(128, input_dim=8, activation='relu'))

model.add(Dense(64,  activation='relu'))

model.add(Dense(32, activation='relu'))

model.add(Dense(16, activation='relu'))

model.add(Dense(8, activation='relu'))

model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the keras model on the dataset
model.fit(X, y, epochs=400, batch_size=10)

# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))
