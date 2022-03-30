import tensorflow as tf
from read_data import get_data
from sklearn.model_selection import train_test_split
import numpy as np

if __name__ == "__main__":

    # Get x and y values
    x_values,y_values,attributes = get_data()

    # Split into train and test
    x_train,x_test,y_train,y_test = train_test_split(x_values,y_values,test_size = 0.20)

    
    #NOTE: Here is example neural network code
    #TODO: Figure out how to encode the data and the network structure

    model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(9,1)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1)
    ])

    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=5)
    model.evaluate(x_test, y_test)
