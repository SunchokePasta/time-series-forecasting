import pandas as pd

def load_and_prepare(filepath, date_col='SETTLEMENT_DATE', value_col='ENGLAND_WALES_DEMAND', freq='D'):
    """
    Loads a CSV file, converts the datetime column, 
    sets it as the index, sorts, and resamples.

    Parameters:
    -----------
    filepath : str
        Path to the CSV file
    date_col : str
        Column in the CSV that has the datetime values
    value_col : str
        Column with the target values 
    freq : str
        Resampling frequency: 'D' = daily, 'H' = hourly, etc.

    Returns:
    --------
    pd.DataFrame
        Cleaned dataframe with datetime index and resampled values
    """
    # Load data
    df = pd.read_csv(filepath)

    # Convert to datetime
    df[date_col] = pd.to_datetime(df[date_col])

    # Use datetime as index
    df = df.set_index(date_col).sort_index()

    # Keep only the target column
    df = df[[value_col]]

    # Resample to chosen frequency (e.g. daily sum)
    df = df.resample(freq).sum()

    return df
