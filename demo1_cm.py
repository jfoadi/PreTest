import cluster_maker as cm

df_specs = [
    {'name':'col1', 'reps':[1,2,3,4]},
    {'name':'col2', 'reps':[4.2,5.67]},
    {'name': 'col3', 'reps':[45,67.43,-453.6,-6.54,0.0353]}
]
df = cm.define_dataframe_structure(df_specs)
print("crreating dataframe.ls..")
print(df)

df_dataspecs = {
    'col1': {'distribution':'normal','variance':2.3},
    'col2': {'distribution':'uniform','variance':0.54},
    'col3': {'distribution':'uniform','variance':-5.3}
}
data = cm.simulate_data(df,n_points = 50, col_specs =df_dataspecs,random_state = 90)
print(data)
