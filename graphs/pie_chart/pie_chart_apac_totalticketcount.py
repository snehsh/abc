import pandas as pd
import streamlit as st
import plotly.graph_objects as go

COLOR_MAPPING = {
    'CompanyA': 'brown',
    'CompanyB': 'skyblue',
    'CompanyC': 'green',
    'CompanyD': 'orange'
}

def pie_chart_apac_totalticketcount():
    csv_file_path = '/Users/snehshah/PycharmProjects/Project-Vineet/data/random_data.csv'  # Replace with the path to your CSV file
    df = pd.read_csv(csv_file_path)

    # Filter data for APAC region
    df_apac = df[df['Region'] == 'APAC']
    ticket_counts = df_apac.groupby('Company').size().sort_values(ascending=False)
    ticket_count_df=ticket_counts.reset_index(name='Total Ticket Count')
    ticket_count_df.index=ticket_count_df.index +1



    # Prepare data for Plotly
    labels = ticket_counts.index
    values = ticket_counts.values
    colors = [COLOR_MAPPING.get(company, 'grey') for company in labels]

    # Create the pie chart
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0,
        marker=dict(colors=colors),
        textinfo='label+percent',
        insidetextorientation='auto',  # Adjust text orientation if needed
        texttemplate='<b>%{value} tickets<br>%{percent}</b>'  # Custom formatting
    )])
    fig.update_traces(textfont_size=20)
    # Update layout
    fig.update_layout(
        title_text='Total Ticket Count by Company for APAC Region',
        title_x=0  # Center the title
    )
    # Display the pie chart using Streamlit
    st.plotly_chart(fig)
    st.dataframe(ticket_count_df)


def pie_chart_emea_totalticketcount():
    csv_file_path = '/Users/snehshah/PycharmProjects/Project-Vineet/data/random_data.csv'  # Replace with the path to your CSV file
    df = pd.read_csv(csv_file_path)

    # Filter data for EMEA region
    df_emea = df[df['Region'] == 'EMEA']
    ticket_counts = df_emea.groupby('Company').size().sort_values(ascending=False)
    ticket_count_df=ticket_counts.reset_index(name='Total Ticket Count')
    ticket_count_df.index=ticket_count_df.index +1

    # Prepare data for Plotly
    labels = ticket_counts.index
    values = ticket_counts.values
    colors = [COLOR_MAPPING.get(company, 'grey') for company in labels]

    # Create the pie chart
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0,
        marker=dict(colors=colors),
        textinfo='label+percent',
        insidetextorientation='auto',  # Adjust text orientation if needed
        texttemplate='<b>%{value} tickets<br>%{percent}</b>'  # Custom formatting
    )])
    fig.update_traces(textfont_size=20)
    # Update layout
    fig.update_layout(
        title_text='Total Ticket Count by Company for EMEA Region',
        title_x=0  # Center the title
    )

    # Display the pie chart using Streamlit
    st.plotly_chart(fig)
    st.dataframe(ticket_count_df)

def pie_chart_cala_totalticketcount():
    csv_file_path = '/Users/snehshah/PycharmProjects/Project-Vineet/data/random_data.csv'  # Replace with the path to your CSV file
    df = pd.read_csv(csv_file_path)

    # Filter data for CALA region
    df_cala = df[df['Region'] == 'CALA']
    ticket_counts = df_cala.groupby('Company').size().sort_values(ascending=False)
    ticket_count_df=ticket_counts.reset_index(name='Total Ticket Count')
    ticket_count_df.index=ticket_count_df.index +1

    # Prepare data for Plotly
    labels = ticket_counts.index
    values = ticket_counts.values
    colors = [COLOR_MAPPING.get(company, 'grey') for company in labels]

    # Create the pie chart
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0,
        marker=dict(colors=colors),
        textinfo='label+percent',
        insidetextorientation='auto',  # Adjust text orientation if needed
        texttemplate='<b>%{value} tickets<br>%{percent}</b>'  # Custom formatting
    )])
    fig.update_traces(textfont_size=20)
    # Update layout
    fig.update_layout(
        title_text='Total Ticket Count by Company for CALA Region',
        title_x=0  # Center the title
    )

    # Display the pie chart using Streamlit
    st.plotly_chart(fig)
    st.dataframe(ticket_count_df)


def pie_chart_nam_totalticketcount():
    csv_file_path = '/Users/snehshah/PycharmProjects/Project-Vineet/data/random_data.csv'  # Replace with the path to your CSV file
    df = pd.read_csv(csv_file_path)

    # Filter data for NAM region
    df_nam = df[df['Region'] == 'NAM']
    ticket_counts = df_nam.groupby('Company').size().sort_values(ascending=False)
    ticket_count_df=ticket_counts.reset_index(name='Total Ticket Count')
    ticket_count_df.index=ticket_count_df.index +1

    # Prepare data for Plotly
    labels = ticket_counts.index
    values = ticket_counts.values
    colors = [COLOR_MAPPING.get(company, 'grey') for company in labels]

    # Create the pie chart
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0,
        marker=dict(colors=colors),
        textinfo='label+percent',
        insidetextorientation='auto',  # Adjust text orientation if needed
        texttemplate='<b>%{value} tickets<br>%{percent}</b>'  # Custom formatting
    )])
    fig.update_traces(textfont_size=20)

    # Update layout
    fig.update_layout(
        title_text='Total Ticket Count by Company for NAM Region',
        title_x=0  # Center the title
    )

    # Display the pie chart using Streamlit
    st.plotly_chart(fig)
    st.dataframe(ticket_count_df)