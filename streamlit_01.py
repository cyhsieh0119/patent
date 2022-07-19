import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Patent Search"
                   ,page_icon="random"
                   ,layout="wide")

st.markdown("# Patent Search page 🎈")
st.sidebar.markdown("# Main page 🎈 of Side Bar")

st.write(st.__version__)
Corp = st.text_input('Please input the keyword of company :', 'apple')
txt=Corp.split(' ')
#
#
if len(txt) >2:
  st.error('Type Error!! Company name need to < 3 ')
else :
  if len(txt)==1:
    link2='https://patents.google.com/xhr/query?url=assignee%3D{}%26country%3DUS%26language%3DENGLISH%26type%3DPATENT%26num%3D100%26sort%3Dnew&exp=&download=true'.format(txt[0])
    patent_data=pd.read_csv(link2,skiprows=1)
  else :
    link2='https://patents.google.com/xhr/query?url=assignee%3D{}%2B{}%26country%3DUS%26language%3DENGLISH%26type%3DPATENT%26num%3D100%26sort%3Dnew&exp=&download=true'.format(txt[0],txt[1])
    patent_data=pd.read_csv(link2,skiprows=1)
  #
  option = st.selectbox(
     'Please choose the item：',
     ('priority date', 'filing/creation date', 'publication date'))
  #
  columns1=['id', 'title', 'priority date', 'filing/creation date', 'publication date', 'grant date', 'inventor/author',  'assignee']
  new_df=patent_data[columns1]
  new_df['filing/year']=patent_data[filing/creation date].str[0:4]
  df=new_df.sort_values(by=option,ascending=False).set_index(option)
  #
  fig = px.histogram(new_df1, x="filing/year")
  #
  col1, col2 = st.columns([2, 1])
  col1.write(df)
  col2.subheader("Patent Filing Trend")
  col2.write(fig)
