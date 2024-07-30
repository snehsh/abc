import streamlit as st
import pandas as pd
import plotly.graph_objects as go

COLOR_MAPPING = {
    'CompanyA': 'brown',
    'CompanyB': 'skyblue',
    'CompanyC': 'green',
    'CompanyD': 'orange'
}


def bar_graph_apac_prod_nonprod():
    csv_file_path = '/Users/snehshah/PycharmProjects/Project-Vineet/data/random_data.csv'
    df = pd.read_csv(csv_file_path)

    # Filter data for APAC region
    df_apac = df[df['Region'] == 'APAC']

    # Create a pivot table to get counts for each company and environment type
    pivot_table = df_apac.pivot_table(index='Company', columns='Env type(prod/nprod)', aggfunc='size', fill_value=0)

    # Prepare the data for Plotly
    companies = pivot_table.index
    prod_counts = pivot_table.get('prod', pd.Series([0] * len(companies), index=companies))
    nprod_counts = pivot_table.get('nprod', pd.Series([0] * len(companies), index=companies))

    # Create the plot
    fig = go.Figure()

    # Add bars for prod
    fig.add_trace(go.Bar(
        x=companies,
        y=prod_counts,
        name='Prod',
        marker_color='skyblue'
    ))

    # Add bars for nprod
    fig.add_trace(go.Bar(
        x=companies,
        y=nprod_counts,
        name='Non-Prod',
        marker_color='orange'
    ))

    # Update layout
    fig.update_layout(
        title='Prod/Non-Prod Distribution',
        title_x=0,
        xaxis_title='Company',
        yaxis_title='Count',
        barmode='group',  # Group bars side by side
        xaxis_tickangle=-45  # Rotate x-axis labels
    )

    # Display the plot using Streamlit
    st.plotly_chart(fig)

def bar_graph_emea_prod_nonprod():
    csv_file_path = '/Users/snehshah/PycharmProjects/Project-Vineet/data/random_data.csv'
    df = pd.read_csv(csv_file_path)

    # Filter data for EMEA region
    df_emea = df[df['Region'] == 'EMEA']

    # Create a pivot table to get counts for each company and environment type
    pivot_table = df_emea.pivot_table(index='Company', columns='Env type(prod/nprod)', aggfunc='size', fill_value=0)

    # Prepare the data for Plotly
    companies = pivot_table.index
    prod_counts = pivot_table.get('prod', pd.Series([0] * len(companies), index=companies))
    nprod_counts = pivot_table.get('nprod', pd.Series([0] * len(companies), index=companies))

    # Create the plot
    fig = go.Figure()

    # Add bars for prod
    fig.add_trace(go.Bar(
        x=companies,
        y=prod_counts,
        name='Prod',
        marker_color='skyblue'
    ))

    # Add bars for nprod
    fig.add_trace(go.Bar(
        x=companies,
        y=nprod_counts,
        name='Non-Prod',
        marker_color='orange'
    ))

    # Update layout
    fig.update_layout(
        title='Prod/Non-Prod Distribution',
        title_x=0,
        xaxis_title='Company',
        yaxis_title='Count',
        barmode='group',  # Group bars side by side
        xaxis_tickangle=-45  # Rotate x-axis labels
    )

    # Display the plot using Streamlit
    st.plotly_chart(fig)


def bar_graph_cala_prod_nonprod():
    csv_file_path = '/Users/snehshah/PycharmProjects/Project-Vineet/data/random_data.csv'
    df = pd.read_csv(csv_file_path)

    # Filter data for CALA region
    df_cala = df[df['Region'] == 'CALA']

    # Create a pivot table to get counts for each company and environment type
    pivot_table = df_cala.pivot_table(index='Company', columns='Env type(prod/nprod)', aggfunc='size', fill_value=0)

    # Prepare the data for Plotly
    companies = pivot_table.index
    prod_counts = pivot_table.get('prod', pd.Series([0] * len(companies), index=companies))
    nprod_counts = pivot_table.get('nprod', pd.Series([0] * len(companies), index=companies))

    # Create the plot
    fig = go.Figure()

    # Add bars for prod
    fig.add_trace(go.Bar(
        x=companies,
        y=prod_counts,
        name='Prod',
        marker_color='skyblue'
    ))

    # Add bars for nprod
    fig.add_trace(go.Bar(
        x=companies,
        y=nprod_counts,
        name='Non-Prod',
        marker_color='orange'
    ))

    # Update layout
    fig.update_layout(
        title='Prod/Non-Prod Distribution',
        title_x=0,
        xaxis_title='Company',
        yaxis_title='Count',
        barmode='group',  # Group bars side by side
        xaxis_tickangle=-45  # Rotate x-axis labels
    )

    # Display the plot using Streamlit
    st.plotly_chart(fig)

def bar_graph_nam_prod_nonprod():
    csv_file_path = '/Users/snehshah/PycharmProjects/Project-Vineet/data/random_data.csv'
    df = pd.read_csv(csv_file_path)

    # Filter data for NAM region
    df_nam = df[df['Region'] == 'NAM']

    # Create a pivot table to get counts for each company and environment type
    pivot_table = df_nam.pivot_table(index='Company', columns='Env type(prod/nprod)', aggfunc='size', fill_value=0)

    # Prepare the data for Plotly
    companies = pivot_table.index
    prod_counts = pivot_table.get('prod', pd.Series([0] * len(companies), index=companies))
    nprod_counts = pivot_table.get('nprod', pd.Series([0] * len(companies), index=companies))

    # Create the plot
    fig = go.Figure()

    # Add bars for prod
    fig.add_trace(go.Bar(
        x=companies,
        y=prod_counts,
        name='Prod',
        marker_color='skyblue'
    ))

    # Add bars for nprod
    fig.add_trace(go.Bar(
        x=companies,
        y=nprod_counts,
        name='Non-Prod',
        marker_color='orange'
    ))

    # Update layout
    fig.update_layout(
        title='Prod/Non-Prod Distribution',
        title_x=0,
        xaxis_title='Company',
        yaxis_title='Count',
        barmode='group',  # Group bars side by side
        xaxis_tickangle=-45  # Rotate x-axis labels
    )

    # Display the plot using Streamlit
    st.plotly_chart(fig)


