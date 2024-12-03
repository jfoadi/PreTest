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
    """
    Define the structure of the DataFrame based on the column specifications. 

    Args: 
    - column_specs: a list of dictionaries, each dictionary contains the following keys:
        - name: the name of the column
        - reps: a list of representative points for the column
    Returns:
    - A DataFrame with the following structure. 
        - The name of each column in the DataFrame corresponds to the value associated to the key 'name' in each dictionary in the column_specs list.
        - The number of rows in the data frame will be equal to the length of the list of representative points in the dictionary with the largest number of representative points.
        - The values in each column are the representative points in the list associated to the key 'reps' in each dictionary in the column_specs list. 
          If the list of representative points is shorter than the list with the largest number of representative points, the remaining values in the column are NaN.
    """
    # Prepare data dictionary
    data = {}
    max_length = 0

    # Find the maximum length of representative points
    for spec in column_specs:
        max_length = max(max_length, len(spec.get('reps', [])))

    for spec in column_specs:
        name = spec['name']
        reps = spec.get('reps', [])
        # Extend numerical columns with NaN to match max_length
        extended_points = reps + [np.nan] * (max_length - len(reps))
        data[name] = extended_points

    return pd.DataFrame(data)

## Function to simulate data
def simulate_data(seed_df, n_points=100, col_specs=None, random_state=None):
    """
    The simulate_data function is used to generate data based on the seed DataFrame. 
    
    args: 
        - seed_df: a DataFrame with the structure defined by the define_dataframe_structure function.
        - n_points: the number of simulated points to generate for each representative point in the seed DataFrame.
        - col_specs: a dictionary that specifies the distribution of the data for each column. If not provided, an error will be raised.
        - random_state: an integer that specifies the random seed for reproducibility. If not provided, the results will not be reproducible.
    return:
        - A DataFrame with the simulated data based on the seed DataFrame and the column specifications where each row represents a simulated point
          and each column represents a feature.
    """
    if random_state is not None:
        np.random.seed(random_state)
    
    simulated_data = []

    for _, representative in seed_df.iterrows():
        for _ in range(n_points):
            simulated_point = {}
            for col in seed_df.columns:
                # Numerical columns: apply column-specific specifications
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
