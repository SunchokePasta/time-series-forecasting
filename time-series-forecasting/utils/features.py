import pandas as pd

def add_lags_and_rolls(df, target_col, lags=(1,7,14), rolls=(3,7,14)):
    """
    Add lag features (yesterday, last week, etc.)
    and rolling averages (short & long history).

    Parameters:
    -----------
    df : pd.DataFrame
        Time series dataframe with datetime index
    target_col : str
        Column to create lag/rolling features from
    lags : tuple
        How many periods back to lag (e.g. 1=1 day ago)
    rolls : tuple
        Window sizes for rolling averages (e.g. 7=last 7 days)

    Returns:
    --------
    pd.DataFrame with new features
    """
    for lag in lags:
        df[f'lag{lag}'] = df[target_col].shift(lag)

    for window in rolls:
        df[f'roll{window}'] = df[target_col].rolling(window).mean()

    return df


def add_calendar(df):
    """
    Add calendar-based features like weekday/weekend, month, holiday.

    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame with datetime index

    Returns:
    --------
    pd.DataFrame with new features
    """
    df['weekday'] = df.index.weekday        # 0 = Monday, 6 = Sunday
    df['is_weekend'] = (df['weekday'] >= 5).astype(int)
    df['month'] = df.index.month

    try:
        import holidays
        uk_holidays = holidays.country_holidays('GB')
        df['is_holiday'] = df.index.normalize().isin(uk_holidays).astype(int)
    except ImportError:
        df['is_holiday'] = 0  # fallback if holidays package not installed

    return df
