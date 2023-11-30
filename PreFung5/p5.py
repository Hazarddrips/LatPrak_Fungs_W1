import matplotlib.pyplot as plt
import numpy as np

sample = np.random.normal(loc=50, scale=5, size=1000)

plt.figure(figsize=(5, 4))
plt.hist(sample, bins= 10, density=True)
plt.show()