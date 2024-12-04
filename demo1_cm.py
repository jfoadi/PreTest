# Demo file to demonstrate the use of cluster_maker module, using all functions.
import cluster_maker as cm

# exception handling for if user does not have necessary packages installed to use cluster_maker
try:
    # create DataFrame structure using define_dataframe_structure, with columns A and B with 3 and 2 representative points, respectively
    demo_df = cm.define_dataframe_structure([{'name': 'A', 'reps': [1, 2, 3]}, {'name': 'B', 'reps': [4, 5]}])

    # simulate data based on the DataFrame structure, with 5 points per representative point, normal distribution for column A and uniform distribution for column B
    data = cm.simulate_data(demo_df, n_points=5, col_specs={'A': {'distribution': 'normal', 'variance': 1.0}, 'B': {'distribution': 'uniform', 'variance': 2.0}}, random_state=42)

    # export the simulated data to a CSV file and print the formatted data using export_to_csv function
    cm.export_to_csv(data, 'simulated_data.csv', delimiter=",", include_index=False)

    # export data into formatted text file using export_formatted function
    cm.export_formatted(data)
    
except ImportError as e:
    print(f"Error importing necessary packages: {e}")

