from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
dataset=loadtxt('books.csv',delimiter=',')

x=dataset.iloc[:,[4,11]].values
y=dataset.iloc[:,3].values
model=Sequential()
model.add(Dense(number_of_neurons,input_dim=8,activation='relu'))
model.add(Dense(number_of_neurons,activation='relu'))
model.add(Dense(number_of_neurons,activation='relu'))
model.add(Dense(number_of_neurons,activation='sigmoid'))
model.summary()
