import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
import streamlit_authenticator as stauth
#from streamlit_folium import folium_static
#import folium

import os
from datetime import datetime
from deta import Deta
import json
import requests

import urllib.request
import urllib.parse
#from trello import TrelloClient, List
from dateutil.parser import parse
from datetime import datetime
import pytz
tz = pytz.timezone('Asia/Singapore')

Users=Deta(os.environ.get('DETA_PROJECT_ID')).Base(os.environ.get('DFC_USERS_BASE'))
pledges=Deta(os.environ.get('DETA_PROJECT_ID')).Base(os.environ.get('DFC_PLEDGES_BASE'))

#@st.cache(suppress_st_warning=True)
def auth_init():

    res = Users.fetch()

    cd = {"usernames" : {} }
    if res.count == 0:
        pass
    else:
        for x in res.items :
            cd['usernames'][x['username']] = {'name' : x['name'], 'password' : x['hash_password'], 'email' : x['email']}
            #hashed_passwords.append(x['hash_password'])
    return cd

st.write("# milynnus Development and Demo! 👋")

if 'authentication_status' not in st.session_state.keys():
    st.session_state['authentication_status'] = False
#st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.

    I am using Streamlit to development code snippets and to put up
    quick demos by taking full advantage of some of the excellent set
    of tools available

    Note that this workspace is secured by Streamlit Authenticator.
    """)

with st.sidebar:

    credentials = auth_init()

    if credentials['usernames'] != {}:
        authenticator = stauth.Authenticate(credentials,
            'dfc_stauth', os.environ.get('DFC_USERS_SIGNATURE'), cookie_expiry_days=30)
        st.info("This application is secured by Streamlit-Authenticator.")

    else:
        st.session_state['authentication_status'] = False
        st.info("Administrator setup is required.")

    #st.session_state['authentication_status'] = authentication_status
    name, authentication_status, username = authenticator.login('Login', 'sidebar')
    st.session_state['authentication_status'] = authentication_status
    st.session_state['name'] = name

    if st.session_state['authentication_status']:
        authenticator.logout('Logout', 'main')
        st.write('Welcome *%s*' % (st.session_state['name']))

    elif st.session_state['authentication_status'] == False:
        st.error('Username/password is incorrect')
    elif st.session_state['authentication_status'] == None:
        st.warning('Please enter your username and password')


if not st.session_state['authentication_status']  :
    st.stop()
else:
    with sidebar :
        st.write("Session State :")
        st.json(st.session_state)
