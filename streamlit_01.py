import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.set_page_config(page_title="Patent Search"
                   ,page_icon="random"
                   ,layout="wide")

st.markdown("# Patent Search page 🎈")
st.sidebar.markdown("# Main page 🎈 of Side Bar")

st.write(st.__version__)
Corp = st.text_input('Please input the keyword of company :', 'apple')

link2='https://patents.google.com/xhr/query?url=assignee%3D{}%26country%3DUS%26language%3DENGLISH%26type%3DPATENT%26num%3D100%26sort%3Dnew&exp=&download=true'.format(Corp)

patent_data=pd.read_csv(link2,skiprows=1)
option = st.selectbox(
     'Please choose the item：',
     ('priority date', 'filing/creation date', 'publication date'))

df=patent_data.sort_values(by=option,ascending=False)
st.write(df)
