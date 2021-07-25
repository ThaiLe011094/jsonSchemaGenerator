import argparse
import json
import sys
from jsonSchema import from_json
from jsonSchema import guess_schema
from jsonGetter import RagicConnector_1


def export():
    json_data = RagicConnector_1().fetch_metric_date()
    result = json.dumps(guess_schema(json_data), indent=2)
    return result
