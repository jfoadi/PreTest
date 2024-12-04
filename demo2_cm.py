# Demo file to demonstrate the use of the function non_globular_cluster from the cluster_maker module
import cluster_maker as cm

# exception handling for if user does not have necessary packages installed to use cluster_maker
try:
    # create DataFrame structure using define_dataframe_structure, with columns A, B, and C with 3, 2, and 3 representative points, respectively
    demo_df = cm.define_dataframe_structure([{'name': 'A', 'reps': [1, 2, 3]}, {'name': 'B', 'reps': [4, 5]}, {'name': 'C', 'reps': [6, 7, 8]}])

    # simulate non-globular data based on the DataFrame structure, with 100 points per representative point, using moons, circles, and gaussian shapes for columns A, B, and C, respectively
    data = cm.non_globular_clusters(demo_df, n_points=100, col_specs={'A':{'shape':'moons', 'noise':0.05}, 'B':{'shape':'circles', 'noise': 0.05}, 'C':{'shape':'gaussian', 'noise':0.05}}, random_state=42)

    # export the non-globular data to a CSV file using export_to_csv function
    cm.export_to_csv(data, 'non_globular_data.csv', delimiter=",", include_index=False)

except ImportError as e:
    print(f"Error importing necessary packages: {e}")


