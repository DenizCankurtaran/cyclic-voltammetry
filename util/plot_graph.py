import streamlit as st
import plotly.graph_objs as go

# Function used to plot the graph for both the graph overview
# and the detail page. It takes the entries along side the
# title of the graph and the respective X and Y Label,
# plotting each individual entry.
def plot_graph(entries, title, x_label, y_label):
    fig = go.Figure()
    for entry in entries:
        fig.add_trace(
            go.Scatter(
                x=entry["df"][x_label],
                y=entry["df"][y_label],
                name=entry["identifier"],
                mode="lines",
            )
        )
    fig.update_layout(
        title=title,
        xaxis=dict(title=x_label),
        yaxis=dict(title=y_label)
    )
    st.plotly_chart(fig)