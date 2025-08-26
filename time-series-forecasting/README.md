# Time-Series Forecasting: UK Electricity Demand (Baseline vs ML)

## Motivation
Forecast short-term electricity demand and compare classical SARIMA vs ML (XGBoost).
Relevant to trading and grid operations where load expectations drive positions, hedges, and dispatch.

## Data & Tools
- Data: UK demand (England & Wales), 2025 daily aggregation
- Python, pandas, statsmodels (SARIMA), XGBoost, scikit-learn, matplotlib
- Backtesting with rolling windows

## Method
1. Clean & resample to daily
2. Feature engineering: lags, rolling means, calendar & holidays
3. Models: SARIMA(1,1,1)(1,1,1,7) and XGBoost
4. Train/validation split (time-aware), plus rolling backtests
5. Metrics: MAE, RMSE, MAPE

## Results
- See `reports/metrics_comparison.csv`
- Plots in `reports/figures/`: forecast overlays, rolling MAE, residual ACF

## Why it matters (Trading / Grid)
- Better short-term load forecasts → improved unit commitment, hedging, and risk management
- Identify stress periods (holidays, heatwaves) where errors rise → focus data enrichment (temperature, renewables)

## Limitations & Next Steps
- Add weather (temperature), renewables (wind/solar), holiday names
- Hyperparameter tuning for both models
- Consider Prophet/LSTM; hourly granularity

## Repro
- `pip install -r requirements.txt`
