import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]

# Menambahkan warna dan ukuran titik
colors = ['red', 'green', 'blue', 'orange', 'purple']
sizes = [30, 70, 50, 80, 60]

plt.scatter(x, y, c=colors, s=sizes, alpha=0.8, edgecolors='black', linewidths=1.5, label='Data Points')

# Menambahkan garis trend
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), '--', color='gray', label='Trend Line')

# Menambahkan label sumbu x dan y
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# Menambahkan judul
plt.title('Scatter Plot with Trend Line')

# Menampilkan legenda
plt.legend()

# Menetapkan batas sumbu x dan y
plt.xlim(0, 6)
plt.ylim(0, 10)

# Menampilkan grid
plt.grid(True, linestyle='--', alpha=0.7)

# Menampilkan plot
plt.show()
