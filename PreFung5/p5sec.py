import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Generate a random sample from a normal distribution
sample = np.random.normal(loc=50, scale=5, size=1000)

# Calculate mean and standard deviation of the sample
sample_mean = np.mean(sample)
sample_std = np.std(sample)
print('Mean=%.3f \nStandard Deviation=%.3f' % (sample_mean, sample_std))

# Create a normal distribution object
dist = norm(sample_mean, sample_std)

# Generate values for x-axis
values = np.linspace(30, 70, 1000)

# Calculate the probability density function (PDF) for each value
probabilities = dist.pdf(values)

# Plot histogram of the sample
plt.hist(sample, bins=10, density=True, alpha=0.7, label='Sample Histogram')

# Plot the probability density function (PDF)
plt.plot(values, probabilities, label='Fitted Normal Distribution', color='red')

# Add labels and legend
plt.xlabel('Values')
plt.ylabel('Probability Density')
plt.legend()

# Show the plot
plt.show()
