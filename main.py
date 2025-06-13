import streamlit as st
from jira import getTicketDetails
from loki import getLogData
import json

st.header("Ai Agent Root cause analyzer")


def forLogdata(ticket_id):
    responseLog = getLogData(1748940000,1748940400, ticket_id)
    st.success(f"log data is successfully saved in response_{ticket_id}_masked.json")
    
choice = st.selectbox("choose one", ["enter the ticket id", "enter the details manually"])

@st.fragment()
def procWithJira():
    ticket_id = st.text_input("enter the ticket id here")
    if st.button("fetch"):
        dict = getTicketDetails(ticket_id)
        with st.expander("show the ticket details"):
            st.write(dict)
    if st.button("get the log details for this ticket"):
        forLogdata(ticket_id)

@st.fragment()
def manualentry():
    description  =  st.text_area("describe the incident detaildely", height=250)
    # st.write(description)

if choice == "enter the ticket id":
    procWithJira()

   

elif choice == "enter the details manually":
    manualentry()
    
            

