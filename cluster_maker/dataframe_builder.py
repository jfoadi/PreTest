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
#the function takes in the column specifications, and takes in the maximum length of the representative points.
#it takes in the name of the specification and pads the columns with Nan values to match the length of every column. the length is set to the max length.
def define_dataframe_structure(column_specs):
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
# # this function checks the specification of each column. it checks what kind of distribution it is, and its variance,
# and it simulates the distribution with these details and adds points  to a new dataframe called simulated_data. it also raises valueerrors if the distribution specified is un supported
#and checks if the column has no specifications at all.
def simulate_data(seed_df, n_points=100, col_specs=None, random_state=None):
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

def non_globular_cluster(seed_df, n_points=100, dependency='linear', random_state=None):
    """
    Simulate non-globular clusters by introducing dependencies between columns.

    Parameters:
    seed_df (pd.DataFrame): The seed DataFrame with representative points.
    n_points (int): Number of points to simulate for each representative point.
    dependency (str): Type of dependency ('linear', 'quadratic', 'spiral', etc.).
    random_state (int, optional): Seed for reproducibility.

    Returns:
    pd.DataFrame: A DataFrame containing the simulated non-globular data.
    """
    if random_state is not None:
        np.random.seed(random_state)

    simulated_data = []

    for _, representative in seed_df.iterrows():
        for _ in range(n_points):
            simulated_point = {}
            x = np.random.normal(representative.iloc[0], 1.0)  # Base point for dependencies
            if dependency == 'linear':
                for i, col in enumerate(seed_df.columns):
                    simulated_point[col] = x + i * 0.5
            elif dependency == 'quadratic':
                for i, col in enumerate(seed_df.columns):
                    simulated_point[col] = x**2 + i * 0.1
            elif dependency == 'spiral':
                theta = x * np.pi
                simulated_point[seed_df.columns[0]] = np.cos(theta) * (1 + x)
                simulated_point[seed_df.columns[1]] = np.sin(theta) * (1 + x)
                for col in seed_df.columns[2:]:
                    simulated_point[col] = np.random.normal(0, 1.0)  # Noise for additional columns
            else:
                raise ValueError(f"Unsupported dependency type: {dependency}")
            simulated_data.append(simulated_point)

    return pd.DataFrame(simulated_data)
