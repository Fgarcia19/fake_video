import glob
import cv2
import os
from keras.models import load_model
targets = {"1": 0, "2": 0, "3": 1, "4": 1, "5": 2, "6": 2, "7": 3, "8": 3, "HR_1": 0, "HR_2": 1, "HR_3": 2, "HR_4": 3}

model = load_model('keras_model.h5',compile=False)