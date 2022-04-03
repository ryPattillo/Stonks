'''
This file is a dashboard that allows the user to enter the path of a saved model and stock data
It will display the prediction made by the model
'''
from tensorflow import keras
import streamlit as st
import numpy as np

CLASSES = {
    0: "BUY",
    1: "HOLD",
    2: "SELL"
}

if __name__ == "__main__":
    model = keras.models.load_model('models/my_model')
    st.title("Choose a model")
    path = st.text_input("Model path")

    model = keras.models.load_model(path)
    st.title("Stock Predictor")
    q = st.number_input("Quarter",value = 1)
    o = st.number_input("Open",value = 18)
    h = st.number_input("High",value = 20)
    l = st.number_input("Low",value = 15)
    c = st.number_input("Close",value = 17)
    v = st.number_input("Volume",value = 242963398)
    pcp = st.number_input("Percent Change(price)",value = 3.5)
    pcv = st.number_input("Percent Change (volume)",value = 2.00)
    pwv = st.number_input("Prev week volume",value = 242963398)
    nwo = st.number_input("Next week open",value = 16)
    nwc = st.number_input("Next week close",value = 20)
    dnd = st.number_input("Days next dividend",value = 19)
    pnw = st.number_input("Percent return next week",value = 0.2)
    # create model compatible input from streamlit
    x = np.array([q,o,h,l,c,v,pcp,pcv,pwv,nwo,nwc,dnd,pnw])
    if st.button("Make Prediction"):
        prediction = model.predict(x.reshape(1,13))
        result = CLASSES[np.argmax(prediction, axis = 1)[0]]

        if result == "BUY":
            st.success("Buy this stock now!")

        elif result == "HOLD":
            st.info("Hold the stock!")

        elif result == "SELL":
            st.error("You need to sell!")