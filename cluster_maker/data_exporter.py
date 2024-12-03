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

def export_formatted(df, filename):
    """
    Export a DataFrame to a formatted text file for human readability.

    Parameters:
    df (pd.DataFrame): The DataFrame to export.
    filename (str): The name of the file to export the data to.
    """
    with open(filename, 'w') as file:
        # Write header
        file.write("Formatted Data Export\n")
        file.write("=" * 50 + "\n")
        
        # Write column headers
        col_headers = " | ".join(f"{col:<15}" for col in df.columns)
        file.write(f"Index | {col_headers}\n")
        file.write("-" * 50 + "\n")
        
        # Write rows
        for index, row in df.iterrows():
            formatted_row = " | ".join(f"{str(value):<15}" for value in row)
            file.write(f"{index:<5} | {formatted_row}\n")
        
        file.write("=" * 50 + "\n")
    print(f"Data exported to {filename} as a formatted text file.")