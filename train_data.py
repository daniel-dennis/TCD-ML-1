from sklearn.model_selection import train_test_split
import numpy as np
import keras
from keras.layers import Dense, Flatten, Dropout, Activation

X = np.load('X_data.npy').astype('float32')
Y = np.load('Y_data.npy').astype('float32')


X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=.1, random_state=0)

# inputs = keras.layers.Input(shape=(10))
# x = Flatten()(inputs)
# x = Dense(1000, activation='relu')(x)
# x = Dense(1000, activation='relu')(x)
# x = Dense(1000, activation='relu')(x)

# predictions = Dense(10, activation='softmax')(x)

# # we create the model 
# model = keras.models.Model(inputs=inputs, outputs=predictions)
# opt = keras.optimizers.SGD(lr=0.01, decay=2e-4, momentum=0.995, nesterov=True)

# # setup the optimisation strategy
# model.compile(optimizer=opt,
#               loss='categorical_crossentropy',
#               metrics=['accuracy'])


# model.summary()

# if (model.count_params() > 10000000):    
#     raise("Your model is unecessarily complex, scale down!")