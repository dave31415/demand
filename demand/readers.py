from csv import DictReader
from params import data_dir
from datetime import datetime, timedelta


def read_demand_file(filename=None):
    if filename is None:
        filename = "%s/Demand.csv" % data_dir
    project_list = list(DictReader(open(filename, 'rU')))
    return project_list


def project_realization(project, randomize=False):
    if randomize:
        #TODO: sample properly
        pass
    else:
        start_date_date, end_date_date = calculate_start_end_date(
            project['start_date'],
            project['length_months'])

        realized = {'project_name': project['project_name'],
                    'length_months': project['length_months'],
                    'headcount': project['headcount'],
                    'rate': project['rate'],
                    'start_date_date': start_date_date,
                    'end_date_date': end_date_date,
                    'will_actually_happen': True}

        return realized


def calculate_start_end_date(start_date, length_months):
    date_format = '%m/%d/%y'
    start_date_date = datetime.strptime(start_date, date_format)

    days_per_month = 30.4
    n_days = length_months*days_per_month
    time_delta = timedelta(days=n_days)
    end_date_date = start_date_date + time_delta
    return start_date_date, end_date_date


def forecast_project_by_month(project):
    start_year = project['start_date_date'].year
    start_month = project['start_date_date'].month
    end_year = project['end_date_date'].year
    end_month = project['end_date_date'].month

    year = start_year
    month = start_month

    month_list = []

    while year <= end_year and month <= end_month:
        #TODO: fix this, calculate the right number
        billable_work_days_in_month = 20

        hours_per_day = 8
        hours_in_month_per_worker = billable_work_days_in_month * hours_per_day
        work_hours_in_month = project['headcount'] * hours_in_month_per_worker
        revenue_in_month = work_hours_in_month * project['rate']
        record = {'year': year, 'month': month, "revenue": revenue_in_month}
        month_list.append(record)

        month += 1
        if month == 13:
            year += 1
            month = 1


