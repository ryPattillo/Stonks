import matplotlib.pyplot as plt

def graph_loss(epochs,loss):
    '''Graph the change of loss for each epoch
    '''
    plt.plot(epochs, loss, 'bo', label='Training loss')
    plt.title('Training Loss')
    plt.legend()
    plt.show()

