import tkinter as tk
from tkinter import filedialog
from matplotlib import pyplot as plt
import numpy as np
import random
import math
from regresser_functions import fit_best_curve_and_plot
plt.style.use('ggplot')

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(title="Select sensor data file:")
altitude_path = filedialog.askopenfilename(title="Select altitude data file:")

sensor_content = []
altitude_content = []
with open(file_path, 'r') as file:
    for line in file:
        sensor_content.append(float(line.strip())+random.uniform(-2, 2))

with open(altitude_path, 'r') as file:
    for line in file:
        altitude_content.append(float(line.strip()))

sensor_content = np.array(sensor_content)
altitude_content = np.array(altitude_content)

fit_best_curve_and_plot(altitude_content, sensor_content, "Temperature", "Temperature vs Altitude")

# reg = input("Enter Regression Type: (Linear[1], Polynomial[2], Exponential[3], Logarithmic[4])")
# if reg == '1':
#     a,b = np.polyfit(altitude_content, sensor_content, 1)
#     plt.plot(altitude_content, b+a*altitude_content, color='red')
# elif reg == '2':
#     degree = int(input("Enter Polynomial Degree: "))
#     values = np.polyfit(altitude_content, sensor_content, degree)
#     plt.plot(altitude_content, np.polyval(values, altitude_content), color='red')
# elif reg == '3':
#     offset = 0
#     if min(sensor_content) <= 0:
#         offset = abs(min(sensor_content)) + 1
#         sensor_content = [i+offset for i in sensor_content]

#     a,b = np.polyfit(altitude_content, np.log(sensor_content), 1, w=np.sqrt(sensor_content))
#     if offset:
#         sensor_content = [i-offset for i in sensor_content]
#     plt.plot(altitude_content, b*np.exp(a*altitude_content)-offset, color='red')
    
# elif reg == '4':
#     a,b = np.polyfit(np.log(altitude_content), sensor_content, 1)
#     plt.plot(altitude_content, b+a*np.log(altitude_content), color='red')
# else:
#     print("Invalid Input")
#     exit(1)

# plt.scatter(altitude_content, sensor_content)
# plt.show()
