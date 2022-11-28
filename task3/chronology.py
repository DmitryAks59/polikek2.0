import pandas as pd
import datetime as dt
from datetime import timedelta
import plotly.express as px


class Timeline:
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = pd.to_datetime(start_date)
        if end_date is None:
            self.end_date = (pd.to_datetime(start_date) + timedelta(hours=24))
        else:
            self.end_date = pd.to_datetime(end_date)


    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return f'{self.name} started at {self.start_date}' \
               f' and ended at {self.end_date}'

    def set_description(self, description):
        self.description = description
        return description
