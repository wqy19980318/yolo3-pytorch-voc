import numpy as np
import matplotlib.pyplot as plt

loss = np.loadtxt('loss.txt')
x = loss[:, 0]
y1 = loss[:, 1]
y2 = loss[:, 2]

plt.figure()
plt.plot(x, y1, 'red', label='train loss')
plt.plot(x, y2, 'coral', label='val loss')
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.legend()
plt.show()
