# graphics.py

import matplotlib.pyplot as plt


# Define the plot_clusters function and plot each cluster as a separate color
def plot_clusters(data, labels, title="Cluster Plot"):
    """
    Plot the clusters of data points.

    Parameters:
        data (pd.DataFrame): The DataFrame containing the data points.
        labels (list): List of cluster labels for each data point.
        title (str): Title of the plot (default: "Cluster Plot").

    Returns:
        None
    """
    try:
        # Check if the number of clusters is less than the maximum number of colors
        if max(labels) >= len(plt.cm.tab20.colors):
            print("Warning: Number of clusters exceeds the maximum number of colors available.")
        
        # Create a scatter plot for each cluster
        for cluster in range(max(labels) + 1):
            cluster_data = data[labels == cluster]
            plt.scatter(cluster_data.iloc[:, 0], cluster_data.iloc[:, 1], label=f"Cluster {cluster}")

        plt.title(title)
        plt.xlabel("Feature 1")
        plt.ylabel("Feature 2")
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"An error occurred while plotting clusters: {e}")
