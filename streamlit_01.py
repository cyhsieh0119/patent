import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.markdown("# Patent Search page 🎈")
st.sidebar.markdown("# Main page 🎈 of Side Bar")

st.write(st.__version__)
Corp='Kymeta'
link2='https://patents.google.com/xhr/query?url=assignee%3D{}%26country%3DUS%26language%3DENGLISH%26type%3DPATENT%26num%3D100%26sort%3Dnew&exp=&download=true'.format(Corp)
tt=pd.read_csv(link2,skiprows=1)
option = st.selectbox(
     'Please choose the item：',
     ('priority date', 'filing/creation date', 'publication date'))

t1=tt.sort_values(by=option,ascending=False)
st.write(t1)
