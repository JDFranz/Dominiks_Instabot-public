import pandas as pd
import datetime as dt
import xlsxwriter


class date_time_xlsx_handler():

    def __init__(self,name, columns=[]):
        self.path = f"{name}.xls"
        try:
            self.df=pd.read_excel(self.path, index_col='date', parse_dates=True)
        except FileNotFoundError:
            columns=columns.append('date')
            pd.DataFrame( columns=columns).to_excel(self.path)
            self.df=pd.read_excel(self.path, index_col='date', parse_dates=True)

    def add_row_dumb(self, data={}):
        data.update({'date': pd.DatetimeIndex([dt.datetime.now()])})
        self.df=self.df.append(pd.DataFrame(data).set_index('date'))
        self.df.to_excel(self.path)

    def add_today_smart(self,data={}):
        try:
            today= self.df[str(dt.date.today())]
            print(f" Datapoint for date: {dt.date.today()} (today) exists--> NOT ADDED")
        except KeyError:
            self.add_row_dumb(data)

    def increment_col_today(self,col):
        self.df[str(dt.date.today())][str(col)]+=1

    def check_today(self):
        try:
            today= self.df[str(dt.date.today())]
            cols= today.columns
            return today
        except KeyError:
            print(f"No data for today.")
            return pd.DataFrame()

    def exists_today(self):
        try:
            today= self.df[str(dt.date.today())]
            cols= today.columns
            return True
        except KeyError:
            print(f"No data for today.")
            return False



















