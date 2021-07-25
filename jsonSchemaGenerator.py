import argparse
import json

import sys

from jsonSchema import from_json
from jsonSchema import guess_schema

from jsonGetter import RagicConnector_1


json_data = RagicConnector_1().fetch_metric_date()

def final():
    temp = json.dumps(list(json_data.values()))
    temp = json.loads(temp)
    temp = guess_schema(temp)
    # print(json.loads(str(list(a['items'].values())[1]).replace('\'','\"')))
    result = json.loads(str(list(temp['items'].values())[1]).replace('\'','\"'))
    return result

print(final())