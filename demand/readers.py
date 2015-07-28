from csv import DictReader
from params import data_dir


def read_demand_file(filename=None):
    if filename is None:
        filename = "%s/Demand.csv" % data_dir
    return list(DictReader(open(filename, 'rU')))


