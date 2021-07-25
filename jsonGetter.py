import requests
import json
import ast
import pandas as pd
import numpy as np
import urllib
import json
from datetime import date, datetime, timedelta


class RagicConnector_1:
    def __init__(self):
        self.url = "https://filesamples.com/samples/code/json/sample2.json"
        self.header = "{'Authorization':'replace authentication key in this place'}"
        

    def fetch_metric_date(self):
        EndDate = date.today()
        StartDate = EndDate - timedelta(days=2)
        response1 = requests.get(self.url,
                                 headers=ast.literal_eval(self.header))
        data = json.loads(response1.text)
        return data
