import streamlit as st
if not st.session_state['authentication_status']  :
    st.stop()
else:
    with st.sidebar :
        st.write("Session State :")
        st.json(st.session_state)

import asyncio
from telethon import TelegramClient, events

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 1379563
api_hash = '2b01df6cde6a17328b8d34bc5680188b'

async def main():
  client = TelegramClient('session_name', api_id, api_hash)
  await client.start()
  st.write(client.get_me)

asyncio.run(main())
