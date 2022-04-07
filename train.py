'''
This file is the main training file, running this file will
train a model and the prompt you to save it and view any charts
'''
import tensorflow as tf
from read_data import extract_data
from sklearn.model_selection import train_test_split
import numpy as np
from visualize import graph_loss

def main():

    # required dimensions
    INPUT_DIM = (13,1)
    XTRAIN_DIM = INPUT_DIM[0]
    XTEST_DIM = INPUT_DIM[0]
    YTRAIN_DIM = 3
    YTEST_DIM = 3

    # number of training epochs
    EPOCHS = 50

    # Get x and y values
    x_values,y_values = extract_data()

    # Split into train and test
    x_train,x_test,y_train,y_test = train_test_split(x_values,y_values,test_size = 0.20)

    # ensure dimensions are accurate
    assert x_train.shape[1] ==  XTRAIN_DIM
    assert x_test.shape[1] == XTEST_DIM
    assert y_train.shape[1] ==  YTRAIN_DIM
    assert y_test.shape[1] == YTEST_DIM

    # TODO: figure out layers, activation, and loss function)
    model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(INPUT_DIM)),
    tf.keras.layers.Dense(50,activation="relu"),
    tf.keras.layers.Dense(20,activation="relu"),
    tf.keras.layers.Dense(3,activation = 'softmax'),
    ])
    model.compile(
                optimizer='sgd',
                loss=tf.keras.losses.CategoricalCrossentropy(),
                metrics=['accuracy']
                )

    history = model.fit(x_train, y_train, epochs=EPOCHS)
    model.evaluate(x_test, y_test)
    
    # choose next steps after model training
    print("Would you like to display loss charts?")
    choice = input("[y] yes, [n] no\n")
    if choice == 'y':
        graph_loss(np.arange(0,EPOCHS),history.history['loss'])

    print("Would you like to save the model?")
    choice = input("[y] yes, [n] no\n")
    if choice == 'y':
        path = input("type the path the model should be saved to")
        model.save(path)
main()