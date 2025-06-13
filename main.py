import streamlit as st
from jira import getTicketDetails
from loki import getLogData
import json

st.header("Ai Agent Root cause analyzer")

def forLogdata(ticket_id):
    responseLog = getLogData(1748940000,1748940400, ticket_id)
    st.success(f"log data is successfully saved in response_{ticket_id}_masked.json")
    # st.write("here")
    # if responseLog.status_code == 200:
    #     st.write("got the log data")
    #     if st.button("save to file"):
    #         dictLog =  responseLog.json()
    #         outputLog = open(f"log_{ticket_id}","w" )
    #         json.dump(dictLog, outputLog, indent= 6)
    #         outputLog.close()
    #         st.success(f"saved to file log_{ticket_id}")
    # else:
    #     print(f"Failed to retrieve data. Status code: {responseLog.status_code}, Error: {responseLog.text}")



choice = st.selectbox("choose one", ["enter the ticket id", "entere the details manually"])

@st.fragment()
def procWithJira():
    ticket_id = st.text_input("enter the ticket id here")
    if st.button("fetch"):
        dict = getTicketDetails(ticket_id)
        with st.expander("show the ticket details"):
            st.write(dict)
    if st.button("get the log details for this ticket"):
        forLogdata(ticket_id)

if choice == "enter the ticket id":
    procWithJira()
    
            

