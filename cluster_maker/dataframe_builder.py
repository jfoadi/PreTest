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
    '''
    Constructs a pandas DataFrame with consistent column lengths based on the provided specifications.
    
    This function takes a list of column specifications, each containing a column name and optional representative points. 
    It ensures all columns have the same length by extending shorter columns with NaN values. 
    The maximum length is determined by the longest list of representative points among the columns.
    
    Parameters:
        column_specs (list of dict): 
            A list where each dictionary represents a column specification with:
            - 'name' (str): The column's name.
            - 'reps' (list, optional): A list of representative points (values) for this column. Defaults to an empty list.
    
    Returns:
        pandas.DataFrame: A DataFrame where each column corresponds to a specification from `column_specs`, 
        with all columns having equal lengths, padded with NaN values as necessary.
    '''
    if not isinstance(column_specs, list) or not all(isinstance(spec, dict) for spec in column_specs):
        raise ValueError("column_specs must be a list of dictionaries.")

    # Prepare data dictionary and determine the maximum length
    max_length = max((len(spec.get('reps', [])) for spec in column_specs), default=0)

    data = {}
    for spec in column_specs:
        name = spec.get('name')
        if not name:
            raise ValueError("Each column specification must have a 'name' key.")
        
        reps = spec.get('reps', [])
        extended_points = reps + [np.nan] * (max_length - len(reps))
        data[name] = extended_points

    return pd.DataFrame(data)

## Function to simulate data
def simulate_data(seed_df, n_points=100, col_specs=None, random_state=None):
    '''
    Simulates new data points based on the values of a seed DataFrame, with column-specific distributions.

    This function generates simulated data by perturbing values in the seed DataFrame using specified 
    distributions (normal or uniform) and variances for each column.
    '''
    if not isinstance(seed_df, pd.DataFrame):
        raise ValueError("seed_df must be a pandas DataFrame.")
    
    if col_specs is None or not isinstance(col_specs, dict):
        raise ValueError("col_specs must be provided as a dictionary.")

    if random_state is not None:
        np.random.seed(random_state)

    simulated_data = []
    for _, representative in seed_df.iterrows():
        for _ in range(n_points):
            simulated_point = {}
            for col in seed_df.columns:
                if col in col_specs:
                    dist = col_specs[col].get('distribution', 'normal')
                    variance = col_specs[col].get('variance', 1.0)

                    if dist == 'normal':
                        simulated_point[col] = representative[col] + np.random.normal(0, np.sqrt(variance))
                    elif dist == 'uniform':
                        simulated_point[col] = representative[col] + np.random.uniform(-variance, variance)
                    else:
                        raise ValueError(f"Unsupported distribution: {dist}")
                else:
                    raise ValueError(f"Column '{col}' has no specifications in col_specs.")
            simulated_data.append(simulated_point)

    return pd.DataFrame(simulated_data)

## Function to create non-globular clusters
def non_globular_cluster(seed_df, n_points=100, col_specs=None, random_state=None):
    if not isinstance(seed_df, pd.DataFrame):
        raise ValueError("seed_df must be a pandas DataFrame.")
    
    if random_state is not None:
        np.random.seed(random_state)

    n_clusters = np.random.randint(2, 6)  # Random number of clusters between 2 and 5
    n_dimensions = seed_df.shape[1]

    # Generate random cluster centers
    cluster_centers = np.random.rand(n_clusters, n_dimensions) * 10  # Range [0, 10)

    cluster_points = []
    for center in cluster_centers:
        for _ in range(n_points):
            point = center + np.random.randn(n_dimensions)  # Add random noise
            cluster_points.append(point)

    # Convert to DataFrame
    cluster_df = pd.DataFrame(cluster_points, columns=seed_df.columns)

    # Simulate data based on the generated clusters
    simulated_df = simulate_data(cluster_df, n_points=n_points, col_specs=col_specs, random_state=random_state)

    return simulated_df

 

