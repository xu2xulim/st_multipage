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
url = st.text_input("URL")
st.write("Harrison Thornhill")

with form():
    url = st.text_input("URL")
    submit = st.form_submit_button("Submit")
    if submit:

        URL = f"{url}?apikey=c47h8ZcHRVWABfjr4MukxEMY2Qg25QQfDhFtgKYbkr2aANwwvBKqjVQngCVB9CuNwN3A8PYbvhkkL4UT8g3FZ6XXfR23FDMuTyXF"

        headers = {"Accept": "application/json"}

        response = requests.get(URL, headers=headers)

        st.dataframe(response.json()['items'])
