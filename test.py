import re
filee = open("outest.txt", "w")

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

import json
file  = open("response.json", "r")
data = json.load(file)

masked_dta = loop_nested_json(data)
json_data = json.dumps(masked_dta, indent=4)

outfile = open(f"tesstttt.json", "w")
# json.dump(masked_dta, outfile)
outfile.write(json_data)
print("dumped to file")


