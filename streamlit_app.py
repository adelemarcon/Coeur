import streamlit as st
from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import odeint
import plotly.express as px

st.set_page_config(
   page_title="❤J'ai une petite question❤"
)

st.title("Veux-tu être mon Valentin ?")
st.markdown("### Peut-être que ce graphique peut te convaincre ? ")
st.link_button("Oui", "https://adelemarcon.github.io/DM6adele.html",type="primary",use_container_width=True)
st.link_button("Non", "https://adelemarcon.github.io/DM6adele.html",type="primary",use_container_width=True)

k = st.slider('Slide moi', min_value=0, max_value=3142, step=100)
# Représentation graphique
# ------------------------
x = [i/1000 for i in range (k)]
y = (np.absolute(np.tan(x)))**(np.absolute(1/np.tan(x)))
# En utilisant plotly

fig = px.line(dict(x=x, y=y), x="x", y="y", 
              title = "C'est grâce à toi que mon coeur peut se développer", 
              labels=dict(x="❤", y="❤"),
              height=700,
              template='plotly_white'
)

fig.update_layout(
    margin=dict(l=20, r=40, t=60, b=20),
    paper_bgcolor="white",
    plot_bgcolor='#E4EBEC',
    title_font_color='black',
    title_font_size=20,
    title_font_family='arial',
    title_x=0.5,
    title_xanchor='center',
    font_color='black'
)
fig.update_traces(
    line_color='#2471A3'
)
fig.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black',
    title_font_color='black',
    tickcolor='black',
    tickwidth=2,
    zerolinecolor='white',
    tickfont_color='black',
    showgrid=True,
    gridwidth=1,
    gridcolor='white'
)
fig.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black',
    title_font_color='black',
    tickcolor='black',
    tickwidth=2,
    zerolinecolor='white',
    tickfont_color='black',
    showgrid=True,
    gridwidth=1,
    gridcolor='white'
)
st.plotly_chart(fig, use_container_width=False)
