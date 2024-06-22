import streamlit as st
import plotly.graph_objs as go

def plot_graph(entries, title):
    fig = go.Figure()
    for entry in entries:
        fig.add_trace(
            go.Scatter(
                x=entry["df"]["E"],
                y=entry["df"]["j"],
                name=entry["identifier"],
                mode="lines",
            )
        )
    fig.update_layout(title=title)
    st.plotly_chart(fig)