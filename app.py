import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(layout="wide")
st.title("Esparver viewer")

height = 900
width = 1800

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=37.76,
         longitude=-122.4,
         zoom=11,
         height=height,
         width=width
     ),
     layers=[
         pdk.Layer(
             'ScatterplotLayer',
             data=df,
             get_position='[lon, lat]',
             get_color='[200, 30, 0, 160]',
             get_radius=100,
             auto_highlight=True
         ),
     ],
 ))

