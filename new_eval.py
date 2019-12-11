# import keras
# from keras.models import load_model
# from keras import backend as K
# from keras.layers import Dense
# from keras.models import Model
# from keras import metrics

import tensorflow as tf

import numpy as np
import os
# from tensorflow.keras.models import load_model
import json
import io

# from keras import activations
# from vis.utils import utils


# import keras
# from keras.models import load_model
# from keras.utils import CustomObjectScope
# from keras.initializers import glorot_uniform

def main():
    print('loaded')

    x_test = np.load('./demo_x.npy')
    # with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
    #         model = load_model('./cnn_weights.hdf5')



    model =tf.keras.models.load_model('./cnn_weights.hdf5')

    score = model.predict(x_test)
    final = int(np.argmax(score))
    print(np.argmax(score))
    
    return final
    # return np.argmax(score)


