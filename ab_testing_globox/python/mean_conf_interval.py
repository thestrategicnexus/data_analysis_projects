import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='darkgrid')
# Group A parameters
n_A = 24343
mean_A = 3.375
std_A = 25.94
lower_ci_A = 3.049
upper_ci_A = 3.700

# Group B parameters
n_B = 24600
mean_B = 3.391
std_B = 25.41
lower_ci_B = 3.073
upper_ci_B = 3.708

# Generate data for each group based on normal distribution
data_A = (lower_ci_A, upper_ci_A)
data_B = (lower_ci_B, upper_ci_B)


# Create two separate figures and axes for Group A and Group B
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 3))


# Plot the distribution for Group A
sns.kdeplot(data_A, color='darkslateblue', ax=ax1)
ax1.axvline(mean_A, color='purple', label='Mean')
ax1.get_yaxis().set_visible(False)
ax1.set_frame_on(False)
ax1.axhline(y=0, color='black')
ax1.axvline(lower_ci_A, color='violet', linestyle='--', label='Lower Bound')
ax1.axvline(upper_ci_A, color='violet', linestyle='--', label='Upper Bound')
ax1.set_xlabel('Confidence Interval - Group A')
textstr = f'Mean:{mean_A:.3f}\n' f'Lower bound: {lower_ci_A:.3f}\nUpper bound: {upper_ci_A:.3f}'
#ax1.text(0.05, 0.95, textstr,  fontsize=10)
props = dict(boxstyle='round', facecolor='white', edgecolor='gray', alpha=0.8)
ax1.text(0.05, 0.95,textstr, transform=ax1.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)


# Plot the distribution for Group B
sns.kdeplot(data_B, color='darkslateblue', ax=ax2)
ax2.axvline(mean_B, color='purple', linestyle='-', label='Mean')
ax2.get_yaxis().set_visible(False)
ax2.set_frame_on(False)
ax2.axhline(y=0, color='black')
ax2.axvline(lower_ci_B, color='violet', linestyle='--', label='Lower Bound')
ax2.axvline(upper_ci_B, color='violet', linestyle='--', label='Upper Bound')
ax2.set_xlabel('Confidence Interval - Group B')
textstr = f'Mean:{mean_B:.3f}\n' f'Lower bound: {lower_ci_B:.3f}\nUpper bound: {upper_ci_B:.3f}'
props = dict(boxstyle='round', facecolor='white', edgecolor='gray', alpha=0.8)
ax2.text(0.05, 0.95,textstr, transform=ax2.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)


# Show the plots
plt.tight_layout()
plt.show()
