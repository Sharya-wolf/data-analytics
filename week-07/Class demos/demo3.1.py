# ======================================================================================
# Using Matplotlib to make charts
# Sha'Rya Weaver
# 5/20/2026
# ======================================================================================

# Simple Line Graph
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create line plot
plt.plot(x, y, scalex=True, scaley=True)

# Add labels and title
plt.titles("Simple Line Graph")
plt.xlabel("X values")
plt.ylabel("Y values")

# Display grid (optional but helpful)
plt.grid(True)

# Sow the plot
plt.show()
# ---------------------------------------------------------------------------------------------

# Plot from a pandas DataFrame with markers
import matplotlib.pyplot as plt
import pandas as pd

# Create DataFrame
sales = pd.DataFrame({
    "month": [1, 2, 3, 4, 5, 6],
    "qty_sold": [45, 34, 62, 55, 69, 72]
})

# Plot line graph with markers
plt.plot(
    sales["month"],
    sales["qty_sold"],
    marker = "o" # adds dots on each data point
)

# Title and labels
plt.title("Salees at 6 Months")
plt.xlabel("Month")
plt.ylabel("Quantity Sold")

# Save the graph BEFORE showing it
plt.savefig("the link for the graph")

# Show grid (optional but helpful)
plt.grif(True)

# Display plot
plt.show()























































