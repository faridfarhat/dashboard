# Multi-page Dash Dashboard

A Python Dash application with multiple pages for data analysis.

## Features

- **Distribution Page**: Analyze data distributions with histograms, box plots, and density visualizations
  - Sales distribution analysis
  - Customer age distribution
  - Transaction value distribution

- **Aggregation Page**: Aggregate and visualize data trends
  - Group by category, region, month, or day of week
  - Bar charts, pie charts, and time series trends
  - Summary tables with percentages

## Setup

1. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the dashboard:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:8050`

## Project Structure

```
dashboard/
├── app.py                 # Main application file
├── requirements.txt       # Project dependencies
└── pages/
    ├── distribution.py    # Distribution analysis page
    └── aggregation.py     # Aggregation analysis page
```

## Data

The dashboard uses randomly generated data:
- Sales data with normal distribution
- Customer ages (18-75)
- Transaction values with exponential distribution
- Regional and product category data

## Technologies

- **Dash**: Web framework for building analytical dashboards
- **Plotly**: Interactive visualization library
- **Pandas**: Data manipulation
- **NumPy**: Numerical computing
