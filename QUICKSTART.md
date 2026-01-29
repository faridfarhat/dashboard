# Quick Start Guide

Get your dashboard running in 3 minutes!

## 🚀 Local Installation (First Time)

```bash
# 1. Navigate to dashboard folder
cd /Users/farid/Documents/data_analytics/dashboard/dashboard

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

**Done!** Open http://localhost:8050 in your browser

## 📊 Dashboard Overview

Three powerful analytics pages:

### 1. **Overview** (Default)
See high-level metrics and data samples:
- 5 key metrics cards
- First 5 rows of data
- Sales by region (bar & pie)
- Monthly trends
- Top products & day analysis

### 2. **Aggregation**
Deep dive into your data:
- **Group By**: Region, Month, Day, Product, Quarter, Country, Continent
- **Metrics**: Sales Value, Quantity, Order Count  
- **Filter**: Focus on specific regions
- **Output**: Bar, pie, trend, and summary tables

### 3. **Distribution**
Statistical analysis:
- **Metrics**: Sales Value, Order Quantity, Products
- **Regional Filter**: Compare distributions
- **Charts**: Histogram, box plot, scatter plot
- **Stats**: Mean, median, std dev, quartiles

## 🔄 Workflow

1. **View Overview** → Understand your data at a glance
2. **Use Aggregation** → Find trends and patterns
3. **Analyze Distribution** → Dig into statistical details
4. **Filter & Compare** → Narrow down to specific regions

## 🎯 Quick Tips

- **Change Selections**: Dropdown values update charts instantly
- **Hover on Charts**: See exact values on hover
- **Regional Filter**: Works on both Aggregation and Distribution pages
- **Dynamic Tables**: Summary tables show counts and percentages

## 🌐 Deploying to Render

Ready to share your dashboard? See [DEPLOYMENT.md](DEPLOYMENT.md) for step-by-step instructions.

Quick summary:
1. Create GitHub account (free)
2. Push code to GitHub
3. Connect Render to GitHub repo
4. Set build: `pip install -r requirements.txt`
5. Set start: `gunicorn app:server`
6. Deploy! 🎉

## 📝 File Structure

```
dashboard/
├── app.py              # Main app entry
├── data.py             # Data loading & processing
├── requirements.txt    # Python packages
├── Procfile            # Render config
├── .gitignore          # Git settings
├── DEPLOYMENT.md       # Deploy guide
├── README_FULL.md      # Full documentation
├── QUICKSTART.md       # This file
├── pages/
│   ├── overview.py     # Overview page
│   ├── aggregation.py  # Aggregation page
│   └── distribution.py # Distribution page
└── CSV files           # Your data
```

## 🐛 Common Issues

### "ModuleNotFoundError: No module named 'dash'"
```bash
# Install packages again
pip install -r requirements.txt
```

### "Permission denied" on app.py
```bash
# Make it executable
chmod +x app.py
```

### Charts don't show data
```bash
# Check CSV files exist and are readable
ls -lah *.csv
```

### Port 8050 already in use
```bash
# Run on different port
python app.py --port 8051
```

## 📖 Learn More

- [Dash Docs](https://dash.plotly.com/)
- [Plotly Charts](https://plotly.com/python/)
- [Pandas Guide](https://pandas.pydata.org/docs/)

## ✅ Checklist Before Deploy

- [ ] Tested app locally (`python app.py`)
- [ ] All charts load correctly
- [ ] Filters work as expected
- [ ] CSV files load properly
- [ ] No errors in browser console
- [ ] GitHub account created
- [ ] Render account created
- [ ] Ready to push to GitHub

## 🎉 You're All Set!

Your dashboard is ready to:
- ✅ Run locally
- ✅ Deploy to Render
- ✅ Share with others
- ✅ Analyze your data

**Next**: Follow [DEPLOYMENT.md](DEPLOYMENT.md) to share it online!

---

**Questions?** Check the error message in the terminal or browser console (F12).
