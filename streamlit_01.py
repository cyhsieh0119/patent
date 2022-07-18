import json
import time
import random
import datetime

import requests
import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
 from streamlit_echarts import st_echarts
from streamlit_echarts import st_echarts

from streamlit.server.server import Server
from streamlit.scriptrunner import get_script_run_ctx as get_report_ctx

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

Corp='Kymeta'
link2='https://patents.google.com/xhr/query?url=assignee%3D{}%26country%3DUS%26language%3DENGLISH%26type%3DPATENT%26num%3D100%26sort%3Dnew&exp=&download=true'.format(Corp)
tt=pd.read_csv(link2,skiprows=1)
tt.shape
#print(tt.columns)
