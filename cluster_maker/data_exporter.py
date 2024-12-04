###
## cluster_maker
## A package to simulate clusters of data points.
## J. Foadi - University of Bath - 2024
##
## Module data_exporter
###

## Function to export to CSV
import pandas as pd
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

## Function to export to formatted text file
        
        
def export_formatted(data, filename):
    """
    Export the DataFrame to a formatted text file.

    Parameters:
        data (pd.DataFrame): The DataFrame to export.
        filename (str): Name of the output text file.

    Returns:
        None
    """
    def missing_values(data):
        """
        Calculate the percentage of missing values and zeros in each column of a given DataFrame.
        
        Parameters:
        data (DataFrame): The input DataFrame.
        
        Returns:
        DataFrame: A DataFrame containing the column name, number of unique values, percentage of missing values, and percentage of zeros.
        """
        df = pd.DataFrame()
        for col in list(data):
            unique_values = data[col].unique()
            try:
                unique_values = np.sort(unique_values)
            except:
                pass
            nans = round(pd.isna(data[col]).sum()/data.shape[0]*100,1 )
            zeros = round( (data[col]==0).sum()/data.shape[0]*100,1 )
            df = pd.concat([df, pd.DataFrame([col, len(unique_values), nans, zeros]).T])
        return df.rename(columns={0:'variable',1:'Unique values',2:'Nan %',3:'zeros %'}).sort_values('Nan %', ascending=False)

    df_info = missing_values(data)
    try:
        with open("data/"+filename, 'w') as file:
            file.write(f"Data information:\n\n")
            file.write(f"Number of rows: {data.shape[0]}\n")
            file.write(f"Number of columns: {data.shape[1]}\n\n ")  

            df_info.to_string(file)
            file.write(f"\n\nData:\n\n")
            data.to_string(file)
        print(f"Data successfully exported to {filename}")
    except Exception as e:
        print(f"Error exporting data to formatted text file: {e}")

