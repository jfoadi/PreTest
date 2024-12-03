import cluster_maker as cm


column_specs = [
    {"name": "X_1", "reps": [1, 1, 2, 2]},
    {"name": "X_2", "reps": [3,3.5, 5]}
]

test_data=cm.define_dataframe_structure(column_specs)

print("The column_specs:")
print(column_specs)
print("\nAs we can see a datafram has been created with a NaN added to pad the columns to the same length")
print(test_data)

print("\nNow we will simulate data based on the seed data frame")
print("The seed data frame is the same as the one created above with NaN replaced by 5.5")

test_data["X_2"][3]=5.5

col_specs = {
    "X_1": {"distribution": "normal", "variance": 0.5},
    "X_2": {"distribution": "uniform", "variance": 0.1}
}

seeded_data=cm.simulate_data(test_data, n_points=10, col_specs=col_specs, random_state=None)
print("\nAs we can see, each row of the original test daaframe has had 10 rows of data created seeded on it according to the column specifications")
print(seeded_data)


print("\nWe will now showcase the last funciton which will export the data to a csv file")

cm.export_to_csv(seeded_data, "test_data.csv", delimiter=",", include_index=False)

cm.export_formatted(seeded_data, "test_data.txt")

import numpy as np


##generate non globular data
col_specs =  {
    "X_1": {"func":lambda x: x,},
    "X_2": {"func":lambda x: (4*x)**2+3*x+np.random.uniform(-0.05,0.05)}
}

non_globular_data=cm.non_globular_cluster(test_data, n_points=20, col_specs=col_specs, random_state=None,random_function=np.random.uniform, random_function_params={"low":-0.1, "high":0.1})
print(non_globular_data)

##plot the data
import matplotlib.pyplot as plt
plt.scatter(non_globular_data["X_1"], non_globular_data["X_2"])
plt.show()