# Modeling U.S. National Defense Spending (1962–2023)

**Author**: Mykola Chernyashevskyy  
**Affiliation**: University of Pittsburgh, Department of Physics and Astronomy  
**Email**: myc21@pitt.edu

---

## 🏛️ Introduction

This project explores long-term trends in U.S. **national defense spending** from 1962 to 2023, adjusted to constant FY 2017 dollars. The data reveals both cyclical and linear behavior—capturing both political cycles and long-term increases.

We fit the data using a **combined sinusoidal + linear model** and extract **local maxima and minima** to highlight key turning points in defense budgets. The plot also shades presidential administrations by party to provide historical context.

---

## 📈 Data

- **Source**: U.S. historical budget data for national defense outlays (in constant FY 2017 USD).
- **Years Covered**: 1962–2023
- **Data Shape**:  
  - `year`: 62 time points (1962–2023)  
  - `Spending`: National defense spending (in billions)

---

## 🧪 Methods

### 🔄 Fitting Function

The spending curve is modeled as:

\[
y = A \cdot \sin(Bx + C) + Dx + E
\]

Where:
- `A`: amplitude of oscillation  
- `B`: frequency of oscillation  
- `C`: phase shift  
- `D`: slope of linear trend  
- `E`: intercept

### 📌 Peak Detection

- **Local Maxima**: Identified using `scipy.signal.find_peaks`  
- **Local Minima**: Detected by applying the same method to `-y`  

### 🟦🟥 Administration Highlighting

U.S. presidential administrations are shaded:
- 🟦 **Blue**: Democratic
- 🟥 **Red**: Republican

These intervals are marked using `plt.fill_betweenx`.

---

## 📊 Output

- ⚫ Scatter plot of original spending data  
- 🟢 Sinusoidal + linear best-fit curve  
- ❌ Annotated local peaks (green) and troughs (orange)  
- 📋 Fit equation displayed directly on the plot  
- 🟥🟦 Background shading for political context  

---

## 🧰 Dependencies

Make sure you have the following Python libraries installed:

```bash
pip install numpy matplotlib scipy