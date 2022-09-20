import streamlit as st

import pandas as pd
import os
from deta import Deta

if 'authentication_status' not in st.session_state.keys():
    st.session_state['authentication_status'] = False

if not st.session_state['authentication_status']  :
    st.stop()
else:
    st.title("Overdue Tasks")
    db = Deta(os.environ.get('DEV_PROJECT_ID')).Base('deta_pm_base')
    res = db.fetch({"Status" : "Overdue"})
    df = pd.DataFrame(res.items)
    df_select = df[["Task", "Start Date", "Priority"]]
    st.write(df_select)
    with st.sidebar :

        st.write("Session State : (For Debug Only)")
        #st.json(st.session_state)
