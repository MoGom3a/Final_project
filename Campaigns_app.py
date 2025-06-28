
import streamlit as st
import pandas as pd 
import sklearn
import category_encoders
import joblib

st.set_page_config(layout='wide')

def get_input():
    
    Active_users = st.slider('select Active users on Site' , min_value=1 , max_value=18 ,
                                         value=10 ,step= 1)
    
    Sessions	= st.slider('select Sessions' , min_value=1 , max_value=18 ,
                                         value=10 ,step= 1)
    
    Event_count = st.slider('select Event count' , min_value=1 , max_value=22 ,
                                         value=10 ,step= 1)
    
    Key_events = st.slider('select Key events' , min_value=1 , max_value=20 ,
                                         value=10 ,step= 1)
    return pd.DataFrame(data = [[Active_users, Sessions, Event_count, Key_events]] ,
                 columns=['Active users', 'Sessions', 'Event count', 'Key events'])

test = get_input()

svc = joblib.load('svc.h5')

st.write(svc.predict(test))
