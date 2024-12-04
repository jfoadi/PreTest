###
## cluster_maker
## A package to simulate clusters of data points.
## J. Foadi - University of Bath - 2024
##
## Module dataframe_builder
###

## Libraries needed
import pandas as pd
import numpy as np

## Function to define the wanted data structure
def define_dataframe_structure(column_specs):
    data = {}  # This will hold our column data
    max_length = 0  # To keep track of the longest list of values in the columns

    for spec in column_specs:
        reps = spec.get('reps', [])  # Get the values for the column (or an empty list if none)
        max_length = max(max_length, len(reps))  # Update max_length if this column is longer

    for spec in column_specs:
        name = spec['name']  # Get the name of the column
        reps = spec.get('reps', [])  # Get the values for this column
        
        # If this column is shorter, fill it with NaN values to match the longest column
        extended_points = reps + [np.nan] * (max_length - len(reps))
        
        data[name] = extended_points  # Store the values in the dictionary

    return pd.DataFrame(data)

## Function to simulate data
def simulate_data(seed_df, n_points=100, col_specs=None, random_state=None):
    if random_state is not None:
        np.random.seed(random_state)

    simulated_data = []  # This will hold the new simulated data

    for _, representative in seed_df.iterrows():
        for _ in range(n_points):
            simulated_point = {}  # A dictionary to store the values for the new simulated row
            
            for col in seed_df.columns:
                if col_specs and col in col_specs:
                    dist = col_specs[col].get('distribution', 'normal') 
                    variance = col_specs[col].get('variance', 1.0) 

                    if dist == 'normal':  
                        simulated_point[col] = representative[col] + np.random.normal(0, np.sqrt(variance))
                    elif dist == 'uniform':  
                        simulated_point[col] = representative[col] + np.random.uniform(-variance, variance)
                    else:
                        raise ValueError(f"Unsupported distribution: {dist}")
                else:
                    raise ValueError(f"Column {col} has no specifications in col_specs.")
            
            simulated_data.append(simulated_point)

    return pd.DataFrame(simulated_data)



def non_globular_cluster(seed_df, num_points=100, shape='crescent', noise=0.1, scale=1.0):
    if shape == 'crescent':
        # Generate points in a crescent shape
        angle = np.linspace(0, 2*np.pi, num_points)
        x = np.cos(angle) * scale
        y = np.sin(angle) * scale
        # Add noise to the points
        x += np.random.normal(0, noise, num_points)
        y += np.random.normal(0, noise, num_points)
    elif shape == 'spiral':
        # Generate points in a spiral shape
        angle = np.linspace(0, 5*np.pi, num_points)
        x = angle * np.cos(angle) * scale
        y = angle * np.sin(angle) * scale
        # Add noise to the points
        x += np.random.normal(0, noise, num_points)
        y += np.random.normal(0, noise, num_points)
    else:
        raise ValueError(f"Unsupported shape: {shape}")
    return pd.DataFrame({'x': x, 'y': y})

def export_to_csv(dataframe, filename, delimiter=',', include_index=True):
    dataframe.to_csv(filename, sep=delimiter, index=include_index)








  

    
   