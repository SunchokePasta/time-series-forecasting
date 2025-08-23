import pandas as pd

def add_lags_and_rolls(df, col, lags=(1,7), rolls=(3,7)):
    for k in lags:
        df[f'lag{k}'] = df[col].shift(k)
    for w in rolls:
        df[f'roll{w}'] = df[col].rolling(w, min_periods=1).mean()
    return df

def add_calendar(df):
    df['weekday'] = df.index.weekday
    df['is_weekend'] = (df['weekday'] >= 5).astype(int)
    df['month'] = df.index.month
    df['season'] = ((df['month'] % 12 + 3) // 3)
    return df
