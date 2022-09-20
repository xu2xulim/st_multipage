import streamlit as st
#from io import StringIO
#from trello import TrelloClient
#import pandas as pd
import os
from deta import Deta


if not st.session_state['authentication_status']  :
    st.stop()
else:
    db = Deta(os.environ.get('DEV_PROJECT_ID')).Base('deta_pm_base')
    st.title("Key Project Management Metrics")
    col1, col2, col3 = st.columns(3)

    with col1:
       st.metric("Tasks (Total)", db.fetch().count)

    with col2:
       st.metric("Completed", db.fetch({"Status" : "Completed"}).count)

    with col3:
       st.metric("Overdue", db.fetch({"Status" : "Overdue"}).count)




    with st.sidebar :
        st.write("Session State : (For Debug Only)")
        #st.json(st.session_state)




#client = TrelloClient(api_key = os.environ.get('TRELLO_API_KEY'), token = os.environ.get('TRELLO_TOKEN'))
#client.list_boards()
