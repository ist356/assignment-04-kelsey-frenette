import pandas as pd

def get_column_names(df : pd.DataFrame) -> list[str]: 
    '''
    Get all column names of a pandas dataframe df
    Returns the names as a list of string
    '''
    return df.columns.tolist() #return column names as a list


def get_columns_of_type(df : pd.DataFrame, numpy_type: any) -> list[str]:
    '''
    Return the column names of a pandas dataframe only when 
    the values in the column match the numpy_type
    '''
    columns = [] #initialize an empty list
    for col in df.columns:  #iterate over the columns
        if df[col].dtype == numpy_type: #check if the column type matches numpy_type
            columns.append(col) #add the column name to the list


def get_unique_values(df : pd.DataFrame, column_name: str) -> list:
    '''
    Get a list of unique values of a column in a pandas dataframe
    '''
    return df[column_name].unique().tolist() #return unique values of the column as a list

def get_file_extension(file_path : str) -> str:
    '''
    Return the file extension of a file_path for example:
    '/some/file/data.csv' -> 'csv'
    '/home/important_grades.xlsx' -> 'xlsx'
    'countries.json' -> 'json'

    '''
    return file_path.split('.')[-1] #return the last element of the split string

def load_file(file_path: str, ext: str) -> pd.DataFrame:
    '''
    Load a file into a pandas dataframe assumed the file type from the extension
    return a pandas dataframe
    only suppose csv, excel and json file extensions
    - when csv assume first row is header
    - when json assume record-oriented data
    '''
    if ext == 'csv': #check if the file extension is csv
        return pd.read_csv(file_path, header=0) #read csv file
    elif ext == 'xlsx': #check if the file extension is xlsx
        return pd.read_excel(file_path) #read excel file
    elif ext == 'json': #check if the file extension is json
        return pd.read_json(file_path, orient='records') #read json file
    else:
        return None

if __name__ == '__main__':
    df = pd.DataFrame({ 
        "name": ["Alice", "Bob", "Chris", "Dee", "Eddie", "Fiona"],
        "age": [25, 30, 35, 40, 45, 50],
        "state": ["NY", "PA", "NY", "NY", "PA", "NJ"],
        "balance": [100.0, 200.0, 250.0, 310.0, 100.0, 60.0]
        })
    cols = get_column_names(df) #get column names
    print(f"Columns: {cols}") #print column names
    cols = get_columns_of_type(df, 'object') #get columns of type object
    print(f"Object Columns: {cols}") #print object columns
    cols = get_columns_of_type(df, 'int64') #get columns of type int64
    print(f"Int64 Columns: {cols}") #print int64 columns
    cols = get_columns_of_type(df, 'float64') #get columns of type float64
    print(f"Float64 Columns: {cols}") #print float64 columns
    unique = get_unique_values(df, 'state') #get unique values of state column
    print(f"Unique States: {unique}") #print unique states


