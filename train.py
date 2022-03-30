# import tensorflow as tf
from read_data import get_data, dataset_split

if __name__ == "__main__":

    # Get x and y values
    x_values,y_values,attributes = get_data()

    # Different dataset splits
    train_split = 0.70
    test_split = 0.15
    val_split = 0.15

    # Split into 
    x_train, x_test ,x_val = dataset_split(x_values,train_split,test_split,val_split)
    y_train, y_test ,y_val = dataset_split(y_values,train_split,test_split,val_split)

    '''
    NOTE: Here is example neural network code
    TODO: Figure out how to encode the data and the network structure

    model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(15, 1)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1, activation='softmax')
    ])

    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=5)
    model.evaluate(x_test, y_test)
    '''