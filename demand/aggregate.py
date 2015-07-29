import numpy as np

def agg_revenue_by_month(revenue_data):
    columns_to_agg = ['YEAR', 'MONTH', 'ATL', 'BTL W', 'BTL UW']
    revenue_data_subset = revenue_data[columns_to_agg]
    grouped = revenue_data_subset.groupby(['YEAR', 'MONTH'])
    agg = grouped.aggregate(np.sum)