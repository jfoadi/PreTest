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
from sklearn.datasets import make_moons, make_circles, make_gaussian_quantiles
import matplotlib.pyplot as plt

## Function to define the wanted data structure
def define_dataframe_structure(column_specs):
    """
    Define the structure of the DataFrame based on the column specifications passed as parameter.
    
    Parameters:
        column_specs (list): List of dictionaries with column-specific specifications, with keys 'name' and 'reps'.

    Returns:
        pd.DataFrame: DataFrame with representative points for each column, size len(column_specs) x max_length.
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
    Simulate data points based on the seed DataFrame and column specifications.
    
    Parameters:
        seed_df (pd.DataFrame): Seed DataFrame with representative points.
        n_points (int): Number of points to simulate for each representative point.
        col_specs (dict): Dictionary with column-specific specifications.
        random_state (int): Random seed for reproducibility.

    Returns: 
        pd.DataFrame: Simulated DataFrame with size (n_points * len(seed_df)) x len(seed_df.columns).
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

def non_globular_clusters(seed_df, n_points=100, col_specs=None, random_state=None):
    """
    Simulate data points based on the seed DataFrame and column specifications.

    Parameters:
        seed_df (pd.DataFrame): Seed DataFrame with representative points.
        n_points (int): Number of points to simulate for each representative point.
        col_specs (dict): Dictionary with column-specific specifications, with keys 'shape' (moons, circles, gaussian) and 'noise'.
        random_state (int): Random seed for reproducibility.
    
    Returns:
        pd.DataFrame: Simulated DataFrame with size (n_points * len(seed_df)) x len(seed_df.columns).
    """
    np.random.seed(random_state)

    simulated_data = []
    for _, representative in seed_df.iterrows():
        simulated_point = {}
        for col in seed_df.columns:
            if col_specs and col in col_specs:
                shape = col_specs[col].get('shape', 'moons')
                # Apply column-specific specifications based on shape
                if shape == 'moons':
                    X_moons, Y_moons = make_moons(n_samples=n_points, noise=col_specs[col].get('noise', 0.05), random_state=random_state)
                    simulated_point[col] = X_moons[:, 0] + representative[col]
                    plt.scatter(X_moons[:, 0], X_moons[:, 1], c=Y_moons)
                    plt.tight_layout()
                    plt.savefig(f'{col}_moons.png')
                    plt.close()

                elif shape == 'circles':
                    X_circles, Y_circles = make_circles(n_samples=n_points, noise=col_specs[col].get('noise', 0.05), random_state=random_state)
                    simulated_point[col] = X_circles[:, 0] + representative[col]
                    plt.scatter(X_circles[:, 0], X_circles[:, 1], c=Y_circles)
                    plt.tight_layout()
                    plt.savefig(f'{col}_circles.png')
                    plt.close()

                elif shape == 'gaussian':
                    X_gaussian, Y_gaussian = make_gaussian_quantiles(n_samples=n_points, random_state=random_state)
                    simulated_point[col] = X_gaussian[:, 0] + representative[col]
                    plt.scatter(X_gaussian[:, 0], X_gaussian[:, 1], c=Y_gaussian)
                    plt.tight_layout()
                    plt.savefig(f'{col}_gaussian.png')
                    plt.close()

                else:
                    raise ValueError(f"Unsupported shape: {shape}")
            else:
                raise ValueError(f"Column {col} has no specifications in col_specs.")

        simulated_data.append(simulated_point)
    return pd.DataFrame(simulated_data)


