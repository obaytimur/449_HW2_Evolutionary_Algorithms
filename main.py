# imported libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt
import individual

img_source = cv2.imread("painting.png")
height, width, channel = img_source.shape
