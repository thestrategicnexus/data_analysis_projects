import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Sample size and observations
sample_size = 24343
observations = 955

# Calculate the proportion and conversion rate
proportion = observations / sample_size
conversion_rate = proportion * 100  # Convert to percentage

# Confidence interval
lower_bound = 0.0368
upper_bound = 0.0417

# Generate x-values for the normal distribution curve
x = np.linspace(conversion_rate - 4 * np.sqrt(conversion_rate * (100 - conversion_rate) / sample_size),
                conversion_rate + 4 * np.sqrt(conversion_rate * (100 - conversion_rate) / sample_size), 100)


# Generate the normal distribution curve
y = norm.pdf(x, loc=conversion_rate, scale=np.sqrt(conversion_rate * (100 - conversion_rate) / sample_size))

# Plot the normal distribution curve
plt.plot(x, y, color='darkslateblue')

# Add shaded region for the confidence interval
x_fill = np.linspace(lower_bound * 100, upper_bound * 100, 100)
y_fill = norm.pdf(x_fill, loc=conversion_rate, scale=np.sqrt(conversion_rate * (100 - conversion_rate) / sample_size))
plt.fill_between(x_fill, y_fill, color='lightblue')

# Set the y-axis limits
plt.ylim(0, np.max(y_fill) * 1.1)

# Set labels and title
plt.xlabel("Conversion Rate (%)")
plt.axvline(conversion_rate, color='purple', linestyle='dashed', label='Conversion Rate')


textstr = f'Conversion Rate: {conversion_rate:.2f}% \n' f'Lower bound: {lower_bound:.4f}\nUpper bound: {upper_bound:.4f}'
props = dict(boxstyle='round', facecolor='white', edgecolor='gray', alpha=0.8)
plt.text(3.4, 3.20, textstr, fontsize=9,
         verticalalignment='center', bbox=props)


plt.legend( fontsize=9)

# Remove y-axis ticks
plt.yticks([])

# Display the plot
plt.show()
