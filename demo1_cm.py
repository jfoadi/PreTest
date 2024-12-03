# demo1_cm.py

import cluster_maker as cm
import os

from cluster_maker import (define_dataframe_structure,
                            simulate_data,
                            export_to_csv,
                            export_formatted,
                            non_globular_cluster,
                            plot_clusters)   

def main():
    try:
        location = "C:/Users/david/BathUni/MA50290_24/PreTest/data"
        # Check if the directory exists, create it if not
        if not os.path.exists(location):
            os.makedirs(location)  # Create the directory if it doesn't exist

        # check if the user has the necessary packages installed if not install them
        try:
            import pandas as pd
            import numpy as np
        except ImportError:
            print("The pandas and numpy packages are required for this demo. Installing them...")
            os.system('pip install pandas numpy')
            import pandas as pd
            import numpy as np

        print("Welcome to the Cluster Maker Demo!")
        print("This demo will guide you through defining a DataFrame structure, simulating data, and exporting it.\n")

        print("To access the docstring of each function, use the help function. For example: help(define_dataframe_structure)\n")

        # Step 1: Define the DataFrame structure with more features
        column_specs = [
            {"name": "Feature1", "reps": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]},
            {"name": "Feature2", "reps": [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]},
            {"name": "Feature3", "reps": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]},
            {"name": "Feature4", "reps": [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]},
            {"name": "Feature5", "reps": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]}
        ]
        seed_df = cm.define_dataframe_structure(column_specs)
        print("Initial Seed DataFrame (showing first 10 rows):")
        print(seed_df.head(10))
        print("\n")

        # Step 2: Simulate a larger dataset based on the seed DataFrame
        col_specs = {
            'Feature1': {'distribution': 'normal', 'variance': 4},
            'Feature2': {'distribution': 'uniform', 'variance': 3},
            'Feature3': {'distribution': 'normal', 'variance': 2},
            'Feature4': {'distribution': 'uniform', 'variance': 5},
            'Feature5': {'distribution': 'normal', 'variance': 0.5}
        }

        n_points = 1000  # Increased the number of points to 1000
        simulated_df = cm.simulate_data(seed_df, n_points=n_points, col_specs=col_specs, random_state=42)
        print(f"Simulated DataFrame (first 10 rows of {n_points} points):")
        print(simulated_df.head(10))
        print("\n")

        # Step 3: Generate non-globular clusters (with more data points)
        non_globular_df = cm.non_globular_cluster(seed_df, n_points=n_points, col_specs=col_specs, random_state=42)
        if (non_globular_df is not None):
            print("Non-Globular Cluster DataFrame (first 10 rows):")
            print(non_globular_df.head(10))
            print("\n")
        else:
            print("Non-globular cluster function not yet implemented.\n")

        # Step 4: Export data to CSV
        csv_filename = 'simulated_data_large.csv'
        export_to_csv(simulated_df, location, csv_filename)
        
        # Step 5: Export data to a formatted text file
        formatted_filename = 'formatted_data_large.txt'
        export_formatted(simulated_df, location, formatted_filename)
        
        print("Data export completed. Check the generated files:")
        print(f" - CSV: {csv_filename}")
        print(f" - Formatted Text: {formatted_filename}")

        # Step 6: Plot the clusters (now with more data)
        print("\nPlotting the clusters...")
        # Generate dummy labels for demonstration purposes (replace this with actual clustering labels)
        labels = np.random.randint(0, 5, size=simulated_df.shape[0])  # Make sure the labels array matches the size of the data

        # Ensure that only the first two columns are used for plotting
        plot_clusters(simulated_df.iloc[:, :2], labels, title="Simulated Clusters")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()