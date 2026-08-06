import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)

x = np.array([1,2,3])
y_true = np.array([6,2,4])

# TODO f(x) = w * x
# TODO y = w * x

w = 1.0

# Todo Learning Rate 
lr = 0.01

def loss(w):
    y_pred = w * x
    return np.mean((y_pred - y_true) ** 2)

# Todo dloss=dL/dw

# pd(np.mean((w*x-y_true)**2))/dw

def dloss(w):
    y_pred = w * x
    return np.mean(2 * x * (y_pred - y_true))

print("Start w:", w,"loss:",loss(w))

for step in range(30):
    slope = dloss(w)
    w = w-lr*slope
    print("Step", step + 1, "w:", round(w, 3),"loss: ",loss(w),3)