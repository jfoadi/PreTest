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

"""Add to "data_exporter.py" a function called export_formatted()
##    that exports the data created to a formatted text file. The
##    formatting should make the file human-readable and informative.
# """

def export_formatted(data, filename):
    """
    Export the DataFrame to a formatted text file.

    Parameters:
        data (pd.DataFrame): The DataFrame to export.
        filename (str): Name of the output text file.

    Returns:
        None
    """
    try:
        with open(filename, "w") as file:
            #adds information about each column such as its data type and lengths and if there are any null values to a heder in the file
            file.write("Data Information:\n")
            file.write(f"\tNumber of Data Points: {len(data)}\n\n")
            file.write("Column Information:\n")
            for col in data.columns:
                file.write(f"\tColumn: {col}\n")
                file.write(f"\t\tData Type: {data[col].dtype}\n")
                file.write(f"\t\tNumber of Null Values: {data[col].isnull().sum()}\n")
                file.write(f"\t\tLength: {len(data[col])}\n")
                file.write("\n\n")


            for index, row in data.iterrows():
                file.write(f"Data Point {index}:\n")
                for col, value in row.items():
                    file.write(f"\t{col}: {value}\n")
                file.write("\n")

        print(f"Data successfully exported to {filename}")
    except Exception as e:
        print(f"Error exporting data to formatted text file: {e}")