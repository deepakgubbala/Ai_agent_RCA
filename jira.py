import httpx
import json
# from httpx.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()
import certifi

# # url = "https://your-domain.atlassian.net/rest/api/3/issue/PROJ-123"
# url = "https://adgear.atlassian.net/rest/api/2/issue/PS-4752?fields=description,summary,created"
# # url = "https://adgear.atlassian.net/rest/api/2/issue/PS-4752"

def getTicketDetails(ticketId):
    url = "https://adgear.atlassian.net/rest/api/2/issue/" + ticketId + "?fields=description,summary,created"
    print(url)
    auth = (os.getenv("JIRA_USERNAME"), os.getenv("JIRA_API_KEY"))
    headers = {
        "Accept": "application/json"
    }
    response = httpx.get(url, headers=headers, auth=(os.getenv("JIRA_USERNAME"), os.getenv("JIRA_API_KEY")), verify=False)

    if response.status_code == 200:
        print("got the details succesfuly")  # Ticket details
    else:
        print(f"Error: {response.status_code}, {response.text}")

    dict  = response.json()

    outfile = open("jira.json", "w")
    json.dump(dict, outfile, indent = 6)
    outfile.close()
    return dict

# dict  = getTicketDetails("PS-4752")
