# import matplotlib.pylab as plt
from pathlib import Path
# import os
# import tensorflow_hub as hub

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow import keras
# from tensorflow.keras.models import Sequential
import PIL
import numpy as np
from alert import message

print(tf.__version__)
# tf.contrib.resampler

# export_path = "classify_saved_models/1599549821/"
# # export_path = "classify_Weed_2.h5"

# export_path = Path(export_path)

# global graph

# graph = tf.Graph()

# with graph.as_default():
#     model = tf.keras.models.load_model(export_path)

# model = tf.keras.models.load_model(export_path)

# Load Model

# probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

# Load and prepare Image

size = (1000,1000)

physical_devices = tf.config.list_physical_devices('CPU')
tf.config.set_visible_devices(physical_devices[:], 'CPU')

# export_path = "classify_saved_models/Rice"
export_path = "classify_saved_models/classify_saved_models_rice_log/1604831285"
model = tf.keras.models.load_model(export_path)

# model = tf.keras.models.load_model(export_path)

# Load Model

probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

# graph = tf.compat.v1.get_default_graph()

def predict_rice_weed(image_path, lang):

    image_path = 'temp_images/'+image_path

    im = PIL.Image.open(image_path)
    im = im.resize(size, resample=PIL.Image.LANCZOS)

    # class_names = [
    #     'Cyperus Difformis L', 
    #     'Cyperus Haspan L', 
    #     'Cyperus Iria L',
    #     'Cyperus Rotundus L', 
    #     'Echinochloa Colona (L.) Link',
    #     'Echinochloa Crus-Galli (L.) P. Beauv',
    #     'Eleusine Indica (L.) Gaertner', 
    #     'Enceng (Monochoria Vaginalis)',
    #     'Fimbristylis Miliacea (L.) Vahl', 
    #     'Ipomoea Aquatica Forssk',
    #     'Leptochloa Chinensis (L.) Nees',
    #     'Ludwigia Octovalvis (Jacq.) P.H. Raven', 
    #     'Marsilea Crenata',
    #     'Portulaca Oleracea L', 
    #     'Sphenoclea Zeylanica Gaertner']

    class_names = [
        'Cyperus Difformis L', 'Cyperus Difformis L',
        'Cyperus Haspan L', 'Cyperus Haspan L', 
        'Cyperus Iria L', 'Cyperus Iria L', 
        'Cyperus Rotundus L', 'Cyperus Rotundus L', 
        'Echinochloa Colona (L.) Link', 'Echinochloa Colona (L.) Link',
        'Echinochloa Crus-Galli (L.) P. Beauv', 'Echinochloa Crus-Galli (L.) P. Beauv',
        'Monochoria vaginalis', 
        'Fimbristylis Miliacea (L.) Vahl', 'Fimbristylis Miliacea (L.) Vahl',
        'Ipomoea Aquatica Forssk', 
        'Leptochloa Chinensis (L.) Nees', 'Leptochloa Chinensis (L.) Nees', 
        'Ludwigia adcendes',
        'Ludwigia Octovalvis (Jacq.) P.H. Raven', 'Ludwigia Octovalvis (Jacq.) P.H. Raven',
        'Portulaca Oleracea L', 'Sphenoclea Zeylanica Gaertner']

    img_array = np.array(im).astype(float)
    img_array = np.expand_dims(img_array, axis=0).astype(float)
    # print("img_array.shape\n", img_array.shape)
    # img_array.shape

    print(model.summary())
    # with graph.as_default():
    # predictions = model.predict(img_array)

    predictions = probability_model.predict(img_array)
    print("\n\nGetting Result from Probability Model\n\n")
    print(predictions)

    conf_score = predictions[0][np.argmax(predictions)]

    print("\nconf_score:\n", conf_score)

    if (conf_score>=0.2):
        result = class_names[np.argmax(predictions)]
        # print("Weed Name: ", result)

        return {'result': result}
    else:
        msg_return = message(2, lang)
        return {'message': msg_return}
