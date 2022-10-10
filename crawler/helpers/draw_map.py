import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk


def draw_map(filename: str):
    """
        This function draws a map using the library streamlit and pydeck
    """
    st.header("Air Quality in Spain")
    st.caption("Measuring september's Air Quality")

    df = pd.read_csv(filename)  # CSV containing current air quality

    layer = pdk.Layer(
        'HeatmapLayer',
        data=df,
        opacity=0.9,
        get_position='[lng, lat]',
        # aggregation=String('MEAN'),
        get_weight="avg_val"
    )

    view_state = pdk.ViewState(
        latitude=np.average(50.282187223911),  # Center of the map (Belgium)
        longitude=np.average(5.12971807481202),  # Center of the map (Belgium)
        zoom=7,
        pitch=40.5,
        bearing=-27.36
    )

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=view_state,
        layers=[layer]
    ))

    st.dataframe(df)
