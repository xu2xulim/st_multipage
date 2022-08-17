import streamlit as st
import requests
import pandas as pd

if not st.session_state['authentication_status']  :
    st.stop()
else:
    with st.sidebar :
        st.write("Session State :")
        st.json(st.session_state)

st.write("Harrison Thornhill")
url = "https://dialpad.com/api/v2/contacts?apikey=c47h8ZcHRVWABfjr4MukxEMY2Qg25QQfDhFtgKYbkr2aANwwvBKqjVQngCVB9CuNwN3A8PYbvhkkL4UT8g3FZ6XXfR23FDMuTyXF"

headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)

st.write(response.json()['items'])
