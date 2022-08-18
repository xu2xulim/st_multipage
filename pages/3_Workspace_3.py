import streamlit as st
import requests
import pandas as pd

if 'authentication_status' not in st.session_state.keys():
    st.session_state['authentication_status'] = False

if not st.session_state['authentication_status']  :
    st.stop()
else:
    with st.sidebar :
        st.write("Session State :")
        st.json(st.session_state)

st.write("Harrison Thornhill")
url = "https://getpocket.com/v3/oauth/request"

headers = {"Content-Type": "application/json"}
payload = {
    "consumer_key" : "103406-fe5e558e83e7075fb5c1f39",
    "redirect_uri" : "milynnus:authorizationFinished"
    }
response = requests.get(url, data=payload, headers=headers)

st.write(response)
