import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, column):
    '''
    Plot a histogram for the specified column in the DataFrame.
    '''
    df[column].plot(kind='hist', bins=20)
    plt.title(f"Histogram for {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

def plot_line(df, column):
    '''
    Plot a line graph for the specified column in the DataFrame.
    '''
    df[column].plot(kind='line')
    plt.title(f"Line Plot for {column}")
    plt.xlabel("Index")
    plt.ylabel(column)
    plt.show()

def plot_violin(df, column):
    '''
    Plot a violin plot for the specified column in the DataFrame.
    '''
    sns.violinplot(data=df, y=column)
    plt.title(f"Violin Plot for {column}")
    plt.show()

def plot_box(df, column):
    '''
    Plot a box plot for the specified column in the DataFrame.
    '''
    df.boxplot(column=column)
    plt.title(f"Box Plot for {column}")
    plt.show()

def plot_scatter(df, x_column, y_column):
    '''
    Plot a scatter plot for two specified columns in the DataFrame.
    '''
    df.plot(kind='scatter', x=x_column, y=y_column)
    plt.title(f"Scatter Plot: {x_column} vs {y_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()


def plot_price_histogram(data):
    '''
    Plot histogram for price distribution of products.
    '''
    data['Price'].plot(kind='hist', bins=10, edgecolor='black', alpha=0.7)
    plt.title("Price Distribution")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.show()

def plot_scatter_manufactured_date(data):
    '''
    Plot scatter plot for manufactured date vs price.
    '''
    data.plot(kind='scatter', x='Manufactured Date', y='Price', alpha=0.7)
    plt.title("Price vs Manufactured Date")
    plt.xlabel("Manufactured Date")
    plt.ylabel("Price")
    plt.show()
