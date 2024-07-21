import tensorflow 
from tensorflow import keras
from tensorflow.keras.models import load_model
import numpy as np

def load_train_model():
    model=load_model('Model/best_model.keras')
    return model

def image_preprocess(image):
    # resize the image
    img=image.resize((224,224))
    #  convert to array
    img_array=np.array(img)

    # Expend dimesnion
    img_array=np.expand_dims(img_array,axis=0)

    return img_array

def prediction(image):
    # load the image processor
    image_array=image_preprocess(image=image)

    # load the model
    model=load_train_model()

    # prediction
    y_pred=model.predict(image_array)

    if y_pred>0.5:
        y_pred="Dog"
    else:
        y_pred='Cat'
    
    return y_pred