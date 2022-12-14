import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np 

mnist = tf.keras.datasets.mnist
raw_data = mnist.load_data()
raw_data 

plt.imshow(raw_data[0][0][0], cmap="gray")
raw_data[0][1][0]