import matplotlib.pyplot as plt
import numpy as np

x_1 = np.linspace(0, 5, 10)
y_1 = x_1 ** 2
plt.plot(x_1, y_1)

data = (3, 6, 9, 12, 15)
fig, simple_chart = plt.subplots()

simple_chart.plot(data)
plt.show()
