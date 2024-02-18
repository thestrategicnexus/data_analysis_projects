import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Difference in means and standard error
mean_diff = 0.0163
std_error = 0.232

# Confidence interval values
confidence_mean = 0.455
lower_bound = -0.4386
upper_bound = 0.4714

# t-value and p-value
t_value = 0.0704
p_value = 0.9439

# Calculate the x-values for the difference in means
x = np.linspace(lower_bound, upper_bound, 100)

# Generate the t-distribution curve
y = t.pdf(x, df=48941, loc=mean_diff, scale=std_error)

# Plot the t-distribution curve
plt.plot(x, y, color='darkslateblue')

# Add shaded region for the confidence interval
plt.fill_between(x, y, where=(x >= lower_bound) & (x <= upper_bound), color='lightblue', alpha=0.5)

# Set the x-axis limits
plt.xlim(lower_bound, upper_bound)

# Set labels and title
plt.xlabel("Difference in Means")


# Add annotations for p-value and confidence interval
plt.text((lower_bound + upper_bound) * 0.5, np.max(y) * 0.5,
         f"p-value: {p_value:.4f}\nConfidence Interval: [{lower_bound:.4f}, {upper_bound:.4f}]",
         ha='center')
plt.yticks([])

# Display the plot
plt.show()
