# AdventureWorks Sales Analytics Dashboard

A comprehensive interactive analytics dashboard built with Dash and Plotly to analyze AdventureWorks 2021 sales data.

## 🎯 Features

- **Overview Dashboard**: Summary statistics, key metrics, and high-level visualizations
- **Aggregation Analysis**: Group sales data by region, month, product, country, and more with multiple metrics
- **Distribution Analysis**: Explore statistical distributions with histograms, box plots, and scatter plots
- **Advanced Filtering**: Filter data by region and other dimensions for focused analysis
- **Interactive Visualizations**: Real-time updates with responsive charts and tables

## 🛠️ Technology Stack

- **Frontend**: Dash, Plotly, HTML5, CSS
- **Backend**: Python, Pandas, NumPy
- **Deployment**: Render, Gunicorn
- **Data**: Real AdventureWorks 2021 sales data

## 📋 Installation

### Local Setup

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/sales-analytics-dashboard.git
cd sales-analytics-dashboard/dashboard
```

2. **Create a virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Run the application**:
```bash
python app.py
```

The dashboard will be available at `http://localhost:8050`

## 📁 Project Structure

```
dashboard/
├── app.py                          # Main application entry point
├── data.py                         # Data loading and preprocessing
├── requirements.txt                # Python dependencies
├── Procfile                        # Render deployment configuration
├── .gitignore                      # Git ignore rules
├── README.md                       # This file
├── AdventureWorks Sales Data 2021.csv
├── AdventureWorks Territory Lookup.csv
└── pages/
    ├── __init__.py
    ├── overview.py                 # Dashboard overview page
    ├── aggregation.py              # Sales aggregation analysis
    └── distribution.py             # Statistical distribution analysis
```

## 📊 Data Sources

- **AdventureWorks Sales Data 2021.csv**: Contains 23,000+ order records with:
  - Order dates and stock dates
  - Product keys and customer keys
  - Territory information
  - Order quantities and line items
  
- **AdventureWorks Territory Lookup.csv**: Territory reference data with:
  - Territory keys and region names
  - Country and continent information

## 📈 Dashboard Pages

### 1. Overview
- **Summary Cards**: Key metrics at a glance
  - Total Orders
  - Total Items Ordered
  - Total Sales Value
  - Unique Customers
  - Number of Regions
- **Data Sample**: First 5 rows of the dataset
- **Regional Analysis**:
  - Top regions by sales (bar chart)
  - Sales distribution by region (pie chart)
- **Temporal Analysis**:
  - Monthly sales and order trend (dual-axis line chart)
- **Product & Day Analysis**:
  - Top 10 products by order count
  - Order distribution by day of week

### 2. Aggregation & Analysis
- **Grouping Options** (7 dimensions):
  - By Region
  - By Month
  - By Day of Week
  - By Product
  - By Quarter
  - By Country
  - By Continent

- **Metrics**:
  - Total Sales Value (estimated)
  - Total Order Quantity
  - Order Count

- **Filtering**:
  - Regional filter to focus analysis
  - Dynamic updates in real-time

- **Visualizations**:
  - Bar chart with values
  - Pie chart for distribution
  - Trend lines or category comparison
  - Detailed summary table with percentages

### 3. Distribution Analysis
- **Metric Options**:
  - Sales Value Distribution
  - Order Quantity Distribution
  - Product Distribution

- **Regional Filtering**:
  - Analyze distributions for all regions or specific territories

- **Visualizations**:
  - Histogram (30+ bins) for frequency distribution
  - Box plot with mean and standard deviation
  - Scatter plot showing distribution over time by region
  - Statistical summary table (count, mean, median, std dev, min, max, Q1, Q3)

## 🎓 Key Analytics Features

- **Multi-dimensional Analysis**: Group data by 7 different dimensions for flexible exploration
- **Dynamic Filtering**: Real-time data updates based on user selections
- **Statistical Insights**: Automatic calculation of:
  - Mean, median, and standard deviation
  - Quartiles (Q1, Q3)
  - Min and max values
  - Percentage distribution
- **Trend Analysis**: Time-series visualization of sales patterns and order trends
- **Comparative Analysis**: Regional and product performance comparison
- **Data Quality**: Automatic handling of missing values and data type conversion

## 🚀 Deployment on Render

### Step 1: Prepare for GitHub

1. Initialize git repository (if not already):
```bash
git init
git add .
git commit -m "Initial commit: AdventureWorks Analytics Dashboard"
```

2. Push to GitHub:
```bash
git remote add origin https://github.com/yourusername/sales-analytics-dashboard.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Render

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: sales-analytics-dashboard
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:server`
   - **Instance Type**: Free tier (sufficient for demo), Paid tier recommended for production

5. Click "Create Web Service"
6. Render will automatically deploy your application
7. Your dashboard will be available at: `https://yourdashboard.onrender.com`

### Environment Variables (Optional)
No environment variables required for basic deployment. For production, consider:
- Setting `FLASK_ENV=production`
- Disabling debug mode

## ⚙️ Configuration

### Local Development
- **Port**: 8050
- **Debug Mode**: Enabled (auto-reload on file changes)

### Production (Render)
- **Port**: Auto-assigned by Render
- **Debug Mode**: Disabled for security
- **Gunicorn Workers**: Auto-configured based on dyno size

### Application Settings
- Python version: 3.8 or later
- Data loading: On startup (loaded into memory)
- Caching: Pandas in-memory aggregations

## 🔄 Data Processing Pipeline

The dashboard automatically:

1. **Load Data**: Reads CSV files from disk on application startup
2. **Clean Data**: 
   - Converts OrderDate to datetime format
   - Removes rows with missing critical values
   - Validates OrderQuantity values
3. **Merge Data**: Joins sales data with territory lookup on TerritoryKey
4. **Feature Engineering**:
   - Extracts year, month, quarter, day of week
   - Calculates month names for display
   - Generates estimated sales values based on product and quantity
5. **Aggregate Data**: Performs in-memory aggregations using Pandas for fast results

## 📊 Data Quality Notes

- Dataset contains 23,000+ sales records from 2021
- Some records have missing OrderDate (automatically filtered)
- Territory keys range from 1-10 (10 global regions)
- Product keys provide proxy for product value estimation
- Customer data anonymized by customer key

## ⚡ Performance Considerations

- **Data Loading**: All data loaded on application startup (~1-2 seconds)
- **Aggregation**: In-memory Pandas operations are very fast for this dataset size
- **Response Time**: User interactions should update visualizations in <500ms
- **Scalability**: Dashboard optimized for datasets up to 100,000 rows
- **Browser Compatibility**: Works on modern browsers (Chrome, Firefox, Safari, Edge)

## 🐛 Troubleshooting

### Application won't start
```bash
# Check that dependencies are installed
pip install -r requirements.txt

# Verify CSV files exist
ls -la *.csv

# Check Python version
python --version  # Should be 3.8 or higher
```

### Charts not loading
- Check browser console (F12) for JavaScript errors
- Verify that `data.py` successfully loads CSV files
- Ensure Pandas and Plotly versions are compatible
- Clear browser cache and reload

### Performance issues
- For larger datasets, consider filtering data in `data.py`
- On Render, upgrade to a paid dyno for better performance
- Monitor memory usage with browser DevTools

### Data not updating
- Ensure CSV files are in the same directory as `app.py`
- Check file permissions (should be readable)
- Verify CSV format and column names match code

## 📝 Future Enhancements

- [ ] Export data to CSV/Excel format
- [ ] Custom date range selection with calendar picker
- [ ] Drill-down capabilities for detailed analysis
- [ ] Predictive analytics and forecasting models
- [ ] User authentication and personalized dashboards
- [ ] Real-time data updates with WebSocket
- [ ] Advanced filtering with multiple conditions
- [ ] Custom KPI creation and alerting
- [ ] Mobile-responsive design improvements
- [ ] Dark mode theme support

## 📄 License

MIT License - See LICENSE file for details

## 💬 Support & Contact

For questions, issues, or feature requests, please:
1. Open an issue on GitHub
2. Check existing issues for similar problems
3. Include error messages and browser/system information

## 🙏 Acknowledgments

- AdventureWorks dataset from Microsoft
- Built with [Dash](https://dash.plotly.com/) and [Plotly](https://plotly.com/)
- Inspired by real-world data analytics needs

---

Built with ❤️ using Dash and Plotly

**Last Updated**: January 2026
**Version**: 1.0.0
