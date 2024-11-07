import pandas as pd
import matplotlib.pyplot as plt



# Load the CSV file

data_df = pd.read_csv('dataset.csv')

# Clean column names
data_df.columns = data_df.columns.str.strip()
print("Available columns in the CSV file:")
print(data_df.columns)

# Define columns for each plot
hist_column = 'Age'  # Column for histogram
x_column = 'Height'     # X-axis for scatter plot
y_column = 'Age'        # Y-axis for scatter plot

# Plot histogram
def plot_histogram(data, column, bins=30):
    plt.figure(figsize=(7, 6))
    plt.hist(data[column], bins=bins, color='skyblue', edgecolor='black')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {column}')
    plt.show()

# Plot scatter plot
def plot_scatter(data, x_col, y_col):
    plt.figure(figsize=(7, 6))
    plt.scatter(data[x_col], data[y_col], color='orange')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f'Scatter Plot of {x_col} vs {y_col}')
    plt.show()

# Call the plot functions
plot_histogram(data_df, hist_column)
plot_scatter(data_df, x_column, y_column)