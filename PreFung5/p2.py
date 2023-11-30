import matplotlib.pyplot as plt
import numpy as np

xpoint = np.array([5, 8, 17])
ypoint = np.array([3, 5, 5])

plt.figure(figsize=(8, 6))
plt.plot(xpoint, ypoint, color='red', marker='o', linestyle='-', linewidth=2, markersize=8, label='Data Points')

# Menambahkan judul
plt.title('Plot of Data Points', fontsize=16)

# Menambahkan label sumbu x dan y
plt.xlabel('X-Axis', fontsize=12)
plt.ylabel('Y-Axis', fontsize=12)

# Menambahkan grid
plt.grid(True, linestyle=':', alpha=0.7)

# Menambahkan legenda
plt.legend()

# Menetapkan batas sumbu x dan y
plt.xlim([0, 15])
plt.ylim([0, 15])

# Menampilkan plot
plt.show()
