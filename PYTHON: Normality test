# Before you begin, remember that normality tests are only applicable to quantitative data.
# If you're working with different groups, each with its own data, do not combine the groups. Analyze one group at a time.
# To make the tests work here, you need to import the following libraries:
from scipy.stats import shapiro, normaltest, anderson
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Now, just replace the numbers below with your data of interest:
data = [128, 155, 258, 280, 60, 173, 157, 58, 75, 137, 294, 312, 247, 168, 293, 252, 131, 229,
167, 173, 219, 107, 101, 102, 163, 112, 165, 181, 57, 280, 101, 98, 159, 324, 258, 196, 175,
167, 185, 221, 68, 186, 187, 38, 68, 79, 262, 115, 178, 109, 183, 200, 119, 166]

# Assuming 'data' is the list of your data
mean, std = norm.fit(data)  # Adjusting the parameters of the normal distribution

# Creating the data histogram
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, alpha=0.5, color='red', density=True, label='Histograma dos dados')

# Creating the Superimposed Normal Distribution Curve
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std)
plt.plot(x, p, 'k', linewidth=2, label='Distribuição normal ajustada')

# Configuring the chart
plt.title('Gráfico de normalidade dos valores de PRU')
plt.xlabel('Unidades de reação P2Y12')
plt.ylabel('Densidade')
plt.legend()
plt.grid(True)
plt.show()

# Let's start by subjecting your data to the Shapiro-Wilk test.
# This test evaluates if the data comes from a normal distribution.
stat_shapiro, p_shapiro = shapiro(data)
print("Shapiro-Wilk Test")
print("Test statistic:", stat_shapiro)
print("p-value:", p_shapiro)
print("Conclusion: " + ("Data is not normal." if p_shapiro < 0.05 else "Data is normal.") + "\n")

# Now let's subject the data to the D'Agostino-Pearson test
# This test also checks the normality of the data, but through other parameters: skewness and kurtosis.
stat_dp, p_dp = normaltest(data)
print("D'Agostino-Pearson Test")
print("Test statistic:", stat_dp)
print("p-value:", p_dp)
print("Conclusion: " + ("Data is not normal." if p_dp < 0.05 else "Data is normal.") + "\n")

# Anderson-Darling Test
# This test also assesses normality, but is very sensitive to outliers.
# This test evaluates at various levels of strictness (15%, 10%, 5%, 2.5%, and 1%), yielding different conclusions. Opting for the 1% level implies a stricter assessment, while choosing 15% is more lenient.
result_ad = anderson(data)
print("Anderson-Darling Test")
print("Test statistic:", result_ad.statistic)
print("Critical values:", result_ad.critical_values)
print("Significance levels:", result_ad.significance_level)
# Interpreting the Anderson test result
for i, sig_level in enumerate(result_ad.significance_level):
    if result_ad.statistic > result_ad.critical_values[i]:
        print(f"For a significance level of {sig_level}%, the data is not normal.")
    else:
        print(f"For a significance level of {sig_level}%, the data is normal.")
