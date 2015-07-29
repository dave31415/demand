from params import data_dir
import pandas as pd


def read_revenue(filename=None):
    if filename is None:
        filename = "%s/Revenue.csv" % data_dir
    revenue_data = pd.read_csv(filename)
    revenue_data['Prob_rev'] = revenue_data['PROBABILITY OF REVENUE'].astype('float64')/100.0
    del revenue_data['PROBABILITY OF REVENUE']
    return revenue_data