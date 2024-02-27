from tensorflow.keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import numpy as np
import pandas as pd

img_width = 224
img_height = 224
img_size = (img_width, img_height)
img_channels = 3

# To predict label
# To preprocess image
def img_preprocess(img_path):
    '''
    Apply preprocessing technique to image

    Parameters:
        path of the image

    Returns:
        array of image  
    '''
    img = load_img(img_path, target_size=img_size)
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.
    return img_array

def pred_label(img_array):  
    '''
    Apply preprocessing technique to image

    Parameters:
        array of image

    Returns:
        (class name, confidence) -> string
    '''
    label = pd.read_csv('../artifacts/Predict_Labels')
    label_dict = dict(zip(label['class_name'], label['class_index']))

    model = load_model('../artifacts/Model:Birds_multiclassification.h5')
    pred_prob = model.predict(img_array)
    predicted_class_index = np.argmax(pred_prob)
    confidence = np.max(pred_prob)

    # Map the predicted class index to class name
    class_indices = label_dict
    class_names = list(label_dict.keys())
    predicted_class_name = class_names[predicted_class_index]

    return predicted_class_name, confidence