import pandas as pd
import numpy as np
from datetime import datetime

# Load data files
sales_df = pd.read_csv('AdventureWorks Sales Data 2021.csv')
territory_df = pd.read_csv('AdventureWorks Territory Lookup.csv')

# Data cleaning and preparation
def prepare_data():
    """Load and prepare data for visualizations"""
    
    # Create a copy for processing
    df = sales_df.copy()
    
    # Clean OrderDate - handle missing values
    df['OrderDate'] = pd.to_datetime(df['OrderDate'], format='%m/%d/%Y', errors='coerce')
    
    # Remove rows with missing critical values
    df = df.dropna(subset=['OrderDate', 'OrderQuantity', 'TerritoryKey'])
    
    # Convert OrderQuantity to numeric
    df['OrderQuantity'] = pd.to_numeric(df['OrderQuantity'], errors='coerce')
    df = df[df['OrderQuantity'] > 0]
    
    # Merge with territory information
    df = df.merge(territory_df, left_on='TerritoryKey', right_on='SalesTerritoryKey', how='left')
    
    # Extract time-based features
    df['Year'] = df['OrderDate'].dt.year
    df['Month'] = df['OrderDate'].dt.month
    df['Month_Name'] = df['OrderDate'].dt.strftime('%B')
    df['Quarter'] = df['OrderDate'].dt.quarter
    df['Day_of_Week'] = df['OrderDate'].dt.day_name()
    df['Week'] = df['OrderDate'].dt.isocalendar().week
    
    # Calculate estimated sales value (based on product key as proxy)
    # Assume higher product keys = higher value
    df['EstimatedSalesValue'] = (df['ProductKey'] * df['OrderQuantity'] * 50).astype(float)
    
    return df

# Prepare the main dataframe
df_main = prepare_data()

# Create summary statistics
def get_summary_stats():
    """Get summary statistics of the dataset"""
    total_orders = df_main['OrderNumber'].nunique()
    total_quantity = df_main['OrderQuantity'].sum()
    total_sales_value = df_main['EstimatedSalesValue'].sum()
    unique_customers = df_main['CustomerKey'].nunique()
    unique_products = df_main['ProductKey'].nunique()
    unique_territories = df_main['Region'].nunique()
    
    date_range = f"{df_main['OrderDate'].min().strftime('%B %d, %Y')} to {df_main['OrderDate'].max().strftime('%B %d, %Y')}"
    
    return {
        'total_orders': total_orders,
        'total_quantity': int(total_quantity),
        'total_sales_value': f"${total_sales_value:,.2f}",
        'unique_customers': unique_customers,
        'unique_products': unique_products,
        'unique_territories': unique_territories,
        'date_range': date_range
    }

def get_first_rows(n=5):
    """Get first n rows of the dataset with key columns"""
    cols = ['OrderDate', 'OrderNumber', 'ProductKey', 'CustomerKey', 'Region', 'OrderQuantity', 'EstimatedSalesValue']
    return df_main[cols].head(n)

def get_aggregated_data(group_by, metric='EstimatedSalesValue'):
    """Aggregate data by specified dimension"""
    agg_data = df_main.groupby(group_by)[metric].agg(['sum', 'count', 'mean']).reset_index()
    agg_data.columns = [group_by, 'Total', 'Count', 'Average']
    return agg_data.sort_values('Total', ascending=False)

def get_regional_analysis():
    """Get sales by region"""
    return df_main.groupby('Region').agg({
        'EstimatedSalesValue': 'sum',
        'OrderNumber': 'nunique',
        'OrderQuantity': 'sum',
        'CustomerKey': 'nunique'
    }).rename(columns={
        'EstimatedSalesValue': 'Total_Sales',
        'OrderNumber': 'Order_Count',
        'OrderQuantity': 'Total_Quantity',
        'CustomerKey': 'Customer_Count'
    }).reset_index()

def get_temporal_analysis():
    """Get sales by month"""
    return df_main.groupby('Month_Name').agg({
        'EstimatedSalesValue': 'sum',
        'OrderNumber': 'nunique',
        'OrderQuantity': 'sum'
    }).reset_index()

def get_customer_analysis():
    """Get customer-level metrics"""
    customer_stats = df_main.groupby('CustomerKey').agg({
        'EstimatedSalesValue': 'sum',
        'OrderNumber': 'nunique',
        'OrderQuantity': 'sum',
        'Region': 'first'
    }).rename(columns={
        'EstimatedSalesValue': 'Total_Spent',
        'OrderNumber': 'Order_Count',
        'OrderQuantity': 'Total_Quantity',
        'Region': 'Region'
    }).reset_index()
    return customer_stats

def get_product_analysis():
    """Get product-level metrics"""
    product_stats = df_main.groupby('ProductKey').agg({
        'EstimatedSalesValue': 'sum',
        'OrderNumber': 'nunique',
        'OrderQuantity': 'sum'
    }).rename(columns={
        'EstimatedSalesValue': 'Total_Sales',
        'OrderNumber': 'Order_Count',
        'OrderQuantity': 'Total_Quantity'
    }).reset_index()
    return product_stats.sort_values('Total_Sales', ascending=False)
