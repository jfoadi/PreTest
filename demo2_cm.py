# use of three functions of package cluster_maker
#
import cluster_maker as cm
from cluster_maker.data_exporter import export_formatted
from cluster_maker.dataframe_builder import non_globular_cluster 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

column_specs = [
     {"name": "x", "reps": [1, 2]},
     {"name": "y", "reps": [4, 5]}
]
df = cm.define_dataframe_structure(column_specs)
print(df)
#Simulate data based on the DataFrame structure
seed_df = df
col_specs = {
     "x": {"distribution": "normal", "variance": 0.5},
     "y": {"distribution": "uniform", "variance": 1.0}
}
simulated_data = cm.simulate_data(seed_df, n_points=5, col_specs=col_specs, random_state=42)
print(simulated_data)

#test non globular clusters function
seed_df = pd.DataFrame({
    'x': np.random.normal(0, 1, 100),
    'y': np.random.normal(0, 1, 100)
})
non_globular_data = non_globular_cluster(seed_df, num_points=100, shape='crescent', noise=0.1, scale=1.0)
print(non_globular_data)
#export all results in same text file
#export_formatted([df, simulated_data, non_globular_data], 'export_formatted.txt')

# plot non globular data, one colour 


#plt.scatter(non_globular_data['x'], non_globular_data['y'])









