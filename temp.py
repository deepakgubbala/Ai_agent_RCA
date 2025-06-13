# import requests
import httpx
import json
import os
from dotenv import load_dotenv
load_dotenv()
import re
# from requests.auth import HTTPBasicAuth
print('started')

username = os.getenv("LOKI_USERNAME")
password = os.getenv("LOKI_PASSWORD")


# filee = open("output.txt", "w")
def PII_regex(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    result = re.sub(email_pattern, '[EMAIL]', text)
    return result

def loop_nested_json(obj):
    if isinstance(obj, dict):
        # for key, value in obj.items():
        #     print(f"Key: {key}", file=filee)
            # PII_regex()
            # loop_nested_json(value)
        return {key: loop_nested_json(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        # for item in obj:
        #     loop_nested_json(item)
        return [loop_nested_json(item) for item in obj]
    elif isinstance(obj, str):
        # print(f"Value: {obj}", file=filee)
        # obj = PII_regex(str(obj))
        # print(f"Value_changed: {obj}", file=filee)
        return PII_regex(obj)
    else:
        return obj    

def getLogData(start, end, ticket_id):
    print('started')
    # API endpoint
    url = "https://loki.use1-rprod.k8s.adgear.com/loki/api/v1/query_range?direction=backward"
    payload = {

        'end' : '1748940600',
        'limit' : '10000',
        'query' : "%7Bcluster%3D%22use1-rprod%22%2Cnamespace%3D%22forecasting-backend%22%7D",
        'start' : '1748940000',
        'step' : '1000ms'
    }

    payload['start'] = str(start)
    payload['end'] = str(end)

    for key in payload:
        url = url + '&' +key+'='+ payload[key]
    print(url)
    response = httpx.get(url,  auth = (username, password), verify=False)

    if response.status_code == 200:
        # Parse the JSON data
        # data = response.json(
        print("Data retrieved successfully:")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}, Error: {response.text}")
    dict  = response.json()
    
    # loop_nested_json(dict)
    

    # outfile = open(f"response_{ticket_id}.json", "w")
    # json.dump(dict, outfile, indent = 6)
    masked_dta = loop_nested_json(dict)
    # outfile.close()
    outfile = open(f"response_{ticket_id}_masked.json", "w")
    # json.dump(masked_dta,outfile, indent=4)

    masked_json = json.dumps(masked_dta, indent=4)
    outfile.write(masked_json)
    print("dumped to file")
    # outfile.close()
    
    return response

# api = getLogData(1748940000, 1748940400, "test")
# print(api)



