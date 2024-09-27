import numpy as np

year = [1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

Spending = [117.8, 123, 121.1, 100.2, 109.4, 130.6, 145.6, 141.7, 123.9, 107.8, 99.3, 90.8, 85.9, 83, 79.7, 82.5, 84.2, 89.1, 96.1, 104.3, 116.9, 132.4, 146.7, 166.7, 186.2, 195.7, 190.1, 195.7, 191.3, 180.4, 168.6, 159.7, 140.6, 128.6, 123.2, 120.4, 121, 120.1, 121.8, 130.3, 143.8, 161.1, 178.5, 187.4, 194.4, 206.7, 225.4, 241.2, 245.7, 233.5, 221.8, 204.4, 190.9, 181.8, 183.2, 185.3, 192.5, 213.3, 238.1, 247.1, 232.4, 242.3]

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import find_peaks

# Your data
year = np.array(year)  # Ensure year is a NumPy array for calculations
Spending = np.array(Spending)

initial_guesses = [0, 1/4, 0, 0, 0]

# Define the combined sinusoidal and linear function
def sinusoidal_linear(x, A, B, C, D, E):
    return A * np.sin(B * x + C) + D * x + E

# Fit the data
params, _ = curve_fit(sinusoidal_linear, year, Spending, p0=initial_guesses)

# Generate x values for the fitted curve
x_fit = np.linspace(min(year), max(year), 1000)

# Format the equation string
equation_str = f'y = {params[0]:.2f} * sin({params[1]:.2f}x + {params[2]:.2f}) + {params[3]:.2f}x + {params[4]:.2f}'

# Evaluate the fit equation at x_fit
y_fit = sinusoidal_linear(x_fit, *params)

# Find the indices of the local peaks in y_fit
peaks, _ = find_peaks(y_fit)

# Find the indices of the local minima in y_fit by inverting y_fit
peaks_min, _ = find_peaks(-y_fit)

# Extract the x and y values of the peaks
x_peaks = x_fit[peaks]
y_peaks = y_fit[peaks]

# Extract the x and y values of the minima
x_peaks_min = x_fit[peaks_min]
y_peaks_min = y_fit[peaks_min]

# Plot the data and the fitted curve
plt.figure(figsize=(10, 6))
plt.plot(year, Spending, 'o', label='Original Data',color = "black", linestyle='none')
plt.plot(x_fit, sinusoidal_linear(x_fit, *params), label='Fitted Curve', color='lime', linestyle='--')
plt.xlabel('Fiscal Year')
plt.ylabel('Billions of Constant (FY 2017) Dollars')

# Annotate each peak with its coordinates on the graph
for x_peak, y_peak in zip(x_peaks, y_peaks):
    plt.annotate(f'({x_peak:.2f}, {y_peak:.2f})', (x_peak, y_peak), textcoords="offset points", xytext=(0,10), ha='center')

# Annotate each minima with its coordinates on the graph
for x_peak_min, y_peak_min in zip(x_peaks_min, y_peaks_min):
    plt.annotate(f'({x_peak_min:.2f}, {y_peak_min:.2f})', (x_peak_min, y_peak_min), textcoords="offset points", xytext=(0,-15), ha='center')

plt.plot(x_peaks, y_peaks, 'x', color='green', label='Local Peaks', markersize=10, markeredgewidth=5)
plt.plot(x_peaks_min, y_peaks_min, 'x', color='orange', label='Local Minima',markersize=10, markeredgewidth=5)
plt.title('National Defense Outlays')
# plt.legend()

# Display the equation on the graph
# Adjust the x and y values to position the text appropriately
plt.text(x=1990, y=80, s=equation_str, fontsize=12, bbox=dict(facecolor='white', alpha=0.5))
y_limits = np.arange(50, 250, 1)
plt.fill_betweenx(y_limits, 1961, 1969, color='blue', alpha=0.5)
plt.fill_betweenx(y_limits, 1969, 1977, color='red', alpha=0.5)
plt.fill_betweenx(y_limits, 1977, 1981, color='blue', alpha=0.5)
plt.fill_betweenx(y_limits, 1981, 1993, color='red', alpha=0.5)
plt.fill_betweenx(y_limits, 1993, 2001, color='blue', alpha=0.5)
plt.fill_betweenx(y_limits, 2001, 2009, color='red', alpha=0.5)
plt.fill_betweenx(y_limits, 2009, 2017, color='blue', alpha=0.5)
plt.fill_betweenx(y_limits, 2017, 2021, color='red', alpha=0.5)

plt.show()