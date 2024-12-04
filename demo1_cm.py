
print("""This code prompts the user to define the structure of a DataFrame and simulate data based on the defined structure.
         It then exports the simulated data to a CSV file in the data directory.""")

import cluster_maker as cm


# Define the structure of the DataFrame
column_specs = []
num_columns = int(input("Enter the number of columns: "))

for i in range(num_columns):
    column_name = input(f"Enter the name for column {i+1}: ")
    column_reps = input(f"Enter the repetitions for column {i+1} (comma-separated): ").split(',')
    column_reps = [float(rep) for rep in column_reps]
    column_specs.append({'name': column_name, 'reps': column_reps})

# Define the column specifications for the simulation

col_specs = {}

for column_spec in column_specs:
    column_name = column_spec['name']
    while True:
        column_distribution = input(f"Enter the distribution for column {column_name} (normal/uniform): ")
        if column_distribution.lower() == 'normal' or column_distribution.lower() == 'uniform':
            break
        else:
            print("Invalid input. Please enter 'normal' or 'uniform'.")
    column_variance = float(input(f"Enter the variance for column {column_name}: "))
    col_specs[column_name] = {'distribution': column_distribution, 'variance': column_variance}

# Define the structure of the DataFrame
df = cm.define_dataframe_structure(column_specs)
print("Seed DataFrame:")
print(df)

# Simulate data based on the seed DataFrame
n_points = int(input("Enter the number of data points to simulate: "))
simulated_data = cm.simulate_data(df, n_points=n_points, col_specs=col_specs, random_state=0)
print("Simulated DataFrame:")
print(simulated_data.head())

# Export the data to a CSV file
file_path = input("Enter the filename to export the simulated data into a csv file: ")
cm.export_to_csv(simulated_data, "data/" + file_path + ".csv", delimiter=",", include_index=False)
print("Data exported successfully!")
