import streamlit as st
import requests
import pandas as pd

if 'authentication_status' not in st.session_state.keys():
    st.session_state['authentication_status'] = False

if not st.session_state['authentication_status']  :
    st.stop()
else:
    st.title("Show Eduardo Tasks Instead")
    db = Deta(os.environ.get('DEV_PROJECT_ID')).Base('deta_pm_base')
    res = db.fetch({"Status?ne" : "Completed", "Resources?contains" : "Eduardo Vargas"})
    df = pd.DataFrame(res.items)
    df_select = df[["Task", "Start Date", "Priority", "Resources"]].sort_values(by=['Priority'])
    st.table(df_select)
    with st.sidebar :

        st.write("Session State : (For Debug Only)")
        #st.json(st.session_state)
