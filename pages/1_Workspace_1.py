import streamlit as st
from io import StringIO
from trello import TrelloClient
import pandas as pd
import os

if not st.session_state['authentication_status'] :
    st.stop()
st.warning ("Upload a file like  a CSV to create a list of dictionaries")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     #st.write(bytes_data)

     # To convert to a string based IO:
     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
     #st.write(stringio)

     # To read file as string:
     string_data = stringio.read()
     #st.write(string_data)

     # Can be used wherever a "file-like" object is accepted:
     dataframe = pd.read_csv(uploaded_file)
     st.write(dataframe)
     # Easy way to get a dictitionary from a CSV
     dd = dataframe.to_dict("records")
     #st.json(dd)

client = TrelloClient(api_key = os.environ.get('TRELLO_API_KEY'), token = os.environ.get('TRELLO_TOKEN'))
st.write(client.list_boards())
