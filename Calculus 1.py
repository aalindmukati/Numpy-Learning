import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)

# ? Straight Line

# ? def line_function(x):
# ?  return 2 * x +1

# ? x = np.linspace(-3,3,100)
# ? y = line_function(x)

# ?  slope = rise/run or dy/dx or change in y/change in x

# ? print(x[:5])
# ? print(y[:5])

plt.figure(figsize=(10,6))
# ? plt.plot(x,y)
# ? # plt.show()

# ? x1,x2 = -2,1
# ? y1,y2 = line_function(x1),line_function(x2)
# ? print(y1,y2)

# ? rise = y2 - y1 
# ? run = x2 - x1

# ? slope = rise/run
# ? print('-'*50)
# ? print(f'Point 1 {x1,y1}')
# ? print(f'Point 2 {x2,y2}')
# ? print(f'Rise is {rise}')
# ? print(f'Run is {run}')
# ? print(f'Slope is {slope}')
# ? print('-'*50)

# ! Curve y =X^2

def Curve(z):
    return z**2

x_val = np.linspace(-3,3,200)
y_val = Curve(x_val)
plt.plot(x_val,y_val)
plt.title("Curve")
plt.grid(alpha=0.5)
plt.show()

# ! If we move x a tiny bit and see how much y changes, that change in y divided by change in x gives an approximate slope.

def slope_est(func,x,h=0.00001):
    x2=x+h
    y=Curve(x)
    y2=func(x2)
    dy=y2-y
    dx=h
    slope = dy/dx
    return slope

points = [-2,0,2]

print ("Slope estimates for y=x^2 using small change in x")

for p in points:
    s = slope_est(Curve,p)
    print(f'x={p}->estimated slope is {s:.2f}')