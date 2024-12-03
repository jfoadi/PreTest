# demo1_cm.py

import cluster_maker as cm
import os

from cluster_maker import (define_dataframe_structure,
                            simulate_data,
                            export_to_csv,
                            export_formatted,
                            non_globular_cluster)   

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

        # Step 1: Define the DataFrame structure
        column_specs = [
            {"name": "Feature1", "reps": [10, 20, 30]},
            {"name": "Feature2", "reps": [5, 15]},
            {"name": "Feature3", "reps": [1, 2, 3, 4]}  # Different lengths to show NaN padding
        ]
        seed_df = define_dataframe_structure(column_specs)
        print("Initial Seed DataFrame:")
        print(seed_df)
        print("\n")

        # Step 2: Simulate data based on the seed DataFrame
        col_specs = {
            'Feature1': {'distribution': 'normal', 'variance': 4},
            'Feature2': {'distribution': 'uniform', 'variance': 3},
            'Feature3': {'distribution': 'normal', 'variance': 2}
        }
        simulated_df = simulate_data(seed_df, n_points=5, col_specs=col_specs, random_state=42)
        print("Simulated DataFrame:")
        print(simulated_df.head(10))
        print("\n")

        # Step 3: Generate non-globular clusters
        non_globular_df = non_globular_cluster(seed_df, n_points=5, col_specs=col_specs, random_state=42)
        if (non_globular_df is not None):
            print("Non-Globular Cluster DataFrame:")
            print(non_globular_df.head(10))
            print("\n")
        else:
            print("Non-globular cluster function not yet implemented.\n")

        # Step 4: Export data to CSV
        csv_filename = 'simulated_data.csv'
        export_to_csv(simulated_df, location, csv_filename)
        
        # Step 5: Export data to a formatted text file
        formatted_filename = 'formatted_data.txt'
        export_formatted(simulated_df, location, formatted_filename)
        
        print("Data export completed. Check the generated files:")
        print(f" - CSV: {csv_filename}")
        print(f" - Formatted Text: {formatted_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
