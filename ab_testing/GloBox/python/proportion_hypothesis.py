import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Conversion rates and sample sizes for Group A and Group B
conversion_rate_a = 0.0392
sample_size_a = 24343

conversion_rate_b = 0.0463
sample_size_b = 24600

# Calculate the difference in conversion rates
conversion_rate_diff = conversion_rate_b - conversion_rate_a

# Calculate the pooled standard error
pooled_std_error = np.sqrt((conversion_rate_a * (1 - conversion_rate_a) / sample_size_a) +
                           (conversion_rate_b * (1 - conversion_rate_b) / sample_size_b))

# Calculate the z-score
z_score = conversion_rate_diff / pooled_std_error

# Calculate the p-value
p_value = 2 * (1 - norm.cdf(np.abs(z_score)))

# Calculate the confidence interval
confidence_level = 0.95
alpha = 1 - confidence_level
z_critical = norm.ppf(1 - alpha / 2)
margin_of_error = z_critical * pooled_std_error
confidence_interval = [conversion_rate_diff - margin_of_error, conversion_rate_diff + margin_of_error]

# Generate x-values for the conversion rate difference
x = np.linspace(confidence_interval[0], confidence_interval[1], 100)

# Generate the normal distribution curve
y = norm.pdf(x, loc=conversion_rate_diff, scale=pooled_std_error)

# Plot the normal distribution curve
plt.plot(x, y, color='darkslateblue')

# Add shaded region for the confidence interval
x_fill = np.linspace(confidence_interval[0], confidence_interval[1], 100)
y_fill = norm.pdf(x_fill, loc=conversion_rate_diff, scale=pooled_std_error)

# Set the x-axis limits
plt.xlim(confidence_interval[0], confidence_interval[1])

# Set labels and title
plt.xlabel("Difference in Conversion Rate")

# Add annotations for p-value and confidence interval
plt.text((confidence_interval[0] + confidence_interval[1]) * 0.5, np.max(y_fill) * 0.5,
         f"p-value: {p_value:.4f}\nConfidence Interval: [{confidence_interval[0]:.4f}, {confidence_interval[1]:.4f}]",
         ha='center')

plt.yticks([])
# Display the plot
plt.show()
