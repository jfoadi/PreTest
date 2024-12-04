###
## cluster_maker
## A package to simulate clusters of data points.
## J. Foadi - University of Bath - 2024
##
## Module data_exporter
###

## Function to export to CSV
def export_to_csv(data, filename, delimiter=",", include_index=False):
    """
    Export the DataFrame to a CSV file.

    Parameters:
        data (pd.DataFrame): The DataFrame to export.
        filename (str): Name of the output CSV file.
        delimiter (str): Delimiter for the CSV file (default: ',').
        include_index (bool): Whether to include the DataFrame index (default: False).

    Returns:
        None
    """
    try:
        data.to_csv(filename, sep=delimiter, index=include_index)
        print(f"Data successfully exported to {filename}")
    except Exception as e:
        print(f"Error exporting data to CSV: {e}")

## Function to export to text file
import pandas as pd

def export_formatted(dataframes, file_path="export_formatted_data.txt"):
    try:
        with open(file_path, 'w') as file:
            for i, df in enumerate(dataframes):
                file.write(f"DataFrame {i+1}\n")
                file.write(' | '.join(df.columns) + '\n')
                file.write('-' * (len(df.columns) * 15) + '\n')  # Add a separator line
                
                for index, row in df.iterrows():
                    file.write(' | '.join(map(str, row.values)) + '\n')
                
                file.write('\n')  # Add a newline to separate DataFrames
        
        print(f"Data successfully exported to {file_path}")
    except Exception as e:
        print(f"Error exporting data to text file: {e}")
























