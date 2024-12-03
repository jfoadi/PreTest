###
## cluster_maker
## A package to simulate clusters of data points.
## J. Foadi - University of Bath - 2024
##
## Module data_exporter
###

## Function to export to CSV
def export_to_csv(data, location, filename, delimiter=",", include_index=False):
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


def export_formatted(data, location, filename):
    """
    Exports the DataFrame to a human-readable and informative formatted text file.

    The file includes:
    - A header with metadata (number of rows, columns, and description of the data).
    - A neatly formatted table with column names and values.
    - A footer with summary statistics (e.g., column names, data types).
    
    Parameters:
        data (pd.DataFrame): The DataFrame to be exported.
        filename (str): The name of the text file to export the data.
        
    Returns:
        None
    """
    try:
        with open(filename, 'w') as f:
            # Write header with metadata
            f.write("=== Data Export ===\n")
            f.write(f"Rows: {data.shape[0]}\n")
            f.write(f"Columns: {data.shape[1]}\n")
            f.write(f"Column Names: {', '.join(data.columns)}\n\n")
            
            f.write("=== Data ===\n")
            
            # Calculate column widths
            col_widths = [max(len(str(col)), data[col].astype(str).map(len).max()) for col in data.columns]
            
            # Print header row
            header = ' | '.join([str(col).ljust(col_widths[i]) for i, col in enumerate(data.columns)])
            f.write(header + '\n')
            f.write('-' * len(header) + '\n')
            
            # Print each row with aligned columns
            for _, row in data.iterrows():
                row_str = ' | '.join([str(row[col]).ljust(col_widths[i]) for i, col in enumerate(data.columns)])
                f.write(row_str + '\n')
                
            # Write footer with column types
            f.write("\n=== Footer ===\n")
            for col in data.columns:
                f.write(f"{col}: {data[col].dtype}\n")
            f.write("\nEnd of data export.\n")
            
        print(f"Data successfully exported to {filename}")
    
    except Exception as e:
        print(f"Error exporting data: {e}")
