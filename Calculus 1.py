import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)

def line_function(x):
    return 2 * x +1

x = np.linspace(-3,3,100)
y = line_function(x)

print(x[:5])
print(y[:5])

plt.figure(figsize=(10,6))
plt.plot(x,y)
plt.show()