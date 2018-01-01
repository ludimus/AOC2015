import json
import sys
from pprint import pprint



for line in sys.stdin:
    #print line
    parsed_json=json.loads(line)
    pprint (parsed_json)
   
