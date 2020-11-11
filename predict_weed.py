# import matplotlib.pylab as plt
from pathlib import Path
import os
# import tensorflow_hub as hub
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow import keras
# from tensorflow.keras.models import Sequential
import PIL
import numpy as np

# Disable layout optimizer to not change input data_format.
#tf.config.optimizer.set_experimental_options({'layout_optimizer': False})

# Enable MLIR Graph Optimizations
# tf.config.experimental.enable_mlir_graph_optimization()

# print('tensorflow_version', tf.__version__)
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

export_path = "classify_saved_models/1599549821"
model = tf.keras.models.load_model(export_path)

# ----changed code here (added code for probability model)----
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

# print(model.summary())

def predict(image_path):

    image_path = 'temp_images/'+image_path

    im = PIL.Image.open(image_path).convert('RGB')
    im = im.resize(size, resample=PIL.Image.LANCZOS)

    class_names = [
        'Acalypha indica L.', 
        'Alternanthera philoxeroides (Mart.) Griseb', 
        'Amaranthus viridis Hook. F.', 
        'Amaranthus spinosus L.', 
        'Borreria hispida (L.) K. Schum',
        'Brachiaria erusiformis (J.E.Smith) Griseb', 
        'Brachiaria reptans Gard. and Hubb.', 
        'Celosia argentea L.',
        'Cleome viscosa L.', 
        'Commelina benghalensis L.', 
        'Croton bonplandianum Baill.',
        'Cyperus difformis L.', 
        'Dactyloctenium aegyptium (L.) Willd', 
        'Digera arvensis Forssk.',
        'Digitaria sanguinalis L. (Scop.)', 
        'Dinebra retroflexa (Vahl) Panzer.',
        'Echinochloa colona (L.) Link.', 
        'Echinochloa crusgalli (L.) Beauv.', 
        'Eleusine indica (L.) Gaertner.',
        'Eragrostis pilosa L.', 
        'Euphorbia geniculata Orteg.', 
        'Euphorbia hirta L.',
        'Euphorbia hypersifolia L.', 
        'Euphorbia microphylla Heyneex. Roth.',
        'Parthenium hysterophorus L.', 
        'Phyllanthus niruri L.',
        'Physalis minima L.', 
        'Portulaca oleracea L.', 
        'Stellaria media (L.) Vilt.',
        'Trianthema portulacastrum L.'
    ]

    img_array = np.array(im).astype(float)
    img_array = np.expand_dims(img_array, axis=0).astype(float)
  #  print("\n---img_array.shape---\n", img_array.shape)
  #  print("\n---img_array.type---\n", type(img_array))
    # img_array.shape

  #  print('\n\n---model summary---\n\n')
  #  print(model.summary())

  #  print('\n\n\n------------------------------ model prediction----------------------------- \n\n\n')
  #  print(model.predict(img_array))

#    predictions = model.predict(img_array)
# ----change made here (added code to get prediction from prob model)-------
    predictions = probability_model.predict(img_array)
    print("\n\nGetting Result from Probability Model\n\n")
    print(predictions)

    conf_score = predictions[0][np.argmax(predictions)]

    print("\nconf_score:\n", conf_score)

    if (conf_score>=0.4):
        result = class_names[np.argmax(predictions)]
        # print("Weed Name: ", result)

        return {'result': result}
    else:
        return {'message': "no weed found"}

    # predictions = probability_model.predict(img_array)
# ----Change made here (commented)-----
#    result = class_names[np.argmax(predictions)]
    # print("Weed Name: ", result)

#    return result

