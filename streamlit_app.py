import streamlit as st
from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import odeint
import plotly.express as px

st.set_page_config(
   page_title="❤J'ai une petite question❤"
)

st.title("Veux-tu être mon Valentin ?")
st.link_button("Oui", "https://adelemarcon.github.io/DM6adele.html",type="primary",use_container_width=True)
st.link_button("Non", "https://pourmoncoeur.streamlit.app/",type="primary",use_container_width=True)

st.markdown("### Peut-être que ce graphique peut te convaincre ? ")

k = st.slider('Slide moi', min_value=2200, max_value=3142, step=100)
# Représentation graphique
# ------------------------
theta = [i/1000 for i in range (k)]
th = [i/100 for i in range (3142)]
r = (np.absolute(np.tan(theta)))**(np.absolute(1/np.tan(theta)))
x = r*np.cos(theta)
y = r*np.sin(theta)
# En utilisant plotly

fig = px.line(dict(x=x, y=y), x="x", y="y", 
              title = "C'est grâce à toi que mon coeur peut se développer ❤", 
              height=700,
              template='plotly_white'
)

fig.update_layout(
    margin=dict(l=20, r=40, t=60, b=20),
    paper_bgcolor="white",
    plot_bgcolor='#ece4e4',
    title_font_color='black',
    title_font_size=20,
    title_font_family='arial',
    title_x=0.5,
    title_xanchor='center',
    font_color='#360a0a',
    xaxis_range=[-0.8,0.8],
    yaxis_range = [-0.1,1.4]

    )
fig.update_traces(
   line_width= 10,
   line_color='#ff0000'
)
fig.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=False,
    linecolor='black',
    title_font_color='black',
    tickcolor='black',
    tickwidth=2,
    zerolinecolor='white',
    tickfont_color='black',
    showgrid=False,
    gridwidth=1,
    gridcolor='#ece4e4'
)
fig.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=False,
    linecolor='black',
    title_font_color='black',
    tickcolor='black',
    tickwidth=2,
    zerolinecolor='white',
    tickfont_color='black',
    showgrid=False,
    gridwidth=1,
    gridcolor='#ece4e4'
)
st.plotly_chart(fig, use_container_width=True)
