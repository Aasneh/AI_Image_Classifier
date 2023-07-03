# import pandas as pd
import numpy as np
import tensorflow as tf
# from matplotlib import pyplot as plt
import cv2 as cv
import os
# import PIL
from PIL import Image, ImageOps
# import pickle
# import pathlib
# import seaborn as sns
from tensorflow import keras
from tensorflow.keras import datasets, layers, models
# from tensorflow.keras.preprocessing.image import load_img, img_to_array
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras.models import Model
# from tensorflow.keras.utils import to_categorical, plot_model
# from tensorflow.keras.layers import Input, Dense, LSTM, Embedding, Dropout, add
import streamlit as st

model = keras.models.load_model('./Model.h5')
final={0:'FAKE',1:'REAL'}
pict_size=36

st.title("AI IMAGE CLASSIFIER :brain:")

st.header("GENERAL ARCHITECTURE")
st.image("./model_plot.png")
# test_path="./Testing/"
st.header("TEST IT YOURSELF :smile:")
upload = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
if upload is not None:
    # image_bytes = upload.read()
    # st.image(image_bytes, caption="Uploaded Image", use_column_width=True)
    image = Image.open(upload)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    # with open(os.path.join(test_path,"test.jpg"),"wb") as f: 
    with open("test.jpg","wb") as f: 
      f.write(upload.getbuffer())
    
#     File=os.listdir(test_path)
# #     bytes_data = upload.getvalue()
# #     st.write(bytes_data)
# #     imgpath=""
    Test=[]
#     for file in File:
#         imgpath=os.path.join(test_path,file)
        # if(temp=="test"):
        #     imgpath=temp
    imgpath="./test.jpg"
    img=cv.imread(imgpath)
    new_img=cv.resize(img,(pict_size,pict_size))
    new_img=new_img/255
    Test.append(new_img)
    Test=np.array(Test)
    y_pred=model.predict(Test)
    y_hat=np.argmax(y_pred[0])
    print(final[y_hat])
    st.write(final[y_hat])
    
    ########################################################
    # Test=[]
    # image = Image.open(upload)
    # st.image(image, caption="Uploaded Image", use_column_width=True)
    # # new_img=cv.resize(image,(pict_size,pict_size))
    # image = ImageOps.fit(image,(pict_size,pict_size), Image.ANTIALIAS)
    # # image=image.resize((pict_size,pict_size))
    # new_img = np.array(image)
    # # img_array = img_array.resize((48,48),Image.ANTIALIAS)
    # # print(new_img.shape)
    # new_img=new_img/255
    # Test.append(new_img)
    # Test=np.array(Test)
    # y_pred=model.predict(Test)
    # y_hat=np.argmax(y_pred[0])
    # st.write(final[y_hat])
       
