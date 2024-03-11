import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Function to generate synthetic data
def generate_data():
    years = np.arange(2010, 2021)
    population = np.round(1000000 * (1 + 0.075) ** (years - years[0]))
    housing_demand = population * 0.33
    housing_supply = housing_demand * np.linspace(1.0, 0.95, len(years))
    infrastructure_strain = np.linspace(70, 90, len(years))
    green_space_loss = 100 - np.linspace(100, 80, len(years))

    data = pd.DataFrame({
        'Year': years,
        'Population': population,
        'Housing Demand': housing_demand,
        'Housing Supply': housing_supply,
        'Infrastructure Strain': infrastructure_strain,
        'Green Space Remaining (%)': green_space_loss
    })
    return data

# Load the generated data
data = generate_data()

# Sidebar for navigation
st.sidebar.title('Navigation')
st.sidebar.markdown("**Note:** This app uses simulated data for demonstration purposes.")

section = st.sidebar.radio('Go to', ('Introduction', 'Population Growth', 'Housing Demand vs. Supply', 'Infrastructure Strain', 'Environmental Impact', 'Conclusion'))

# Main app area
st.title('Georgia Housing Trends and Population Growth Analysis')

if section == 'Introduction':
    st.write("""
    ## Introduction
    This analysis explores the dynamics of population growth, housing demand, and their implications for infrastructure and the environment in Georgia.
    """)

elif section == 'Population Growth':
    st.header('Population Growth Trends in Georgia')
    fig_population = px.line(data, x='Year', y='Population', title='Population Growth Over Time')
    st.plotly_chart(fig_population)

elif section == 'Housing Demand vs. Supply':
    st.header('Housing Demand vs. Supply')
    fig_housing = px.line(data, x='Year', y=['Housing Demand', 'Housing Supply'], title='Housing Demand and Supply Over Time')
    st.plotly_chart(fig_housing)

elif section == 'Infrastructure Strain':
    st.header("Infrastructure Strain Over Time")
    fig_infrastructure = px.line(data, x='Year', y='Infrastructure Strain', title='Infrastructure Strain Over Time')
    st.plotly_chart(fig_infrastructure)

elif section == 'Environmental Impact':
    st.header("Environmental Impact of Development")
    fig_environment = px.line(data, x='Year', y='Green Space Remaining (%)', title='Green Space Remaining Over Time')
    st.plotly_chart(fig_environment)

elif section == 'Conclusion':
    st.write("""
    ## Conclusion and Policy Recommendations
    The data presented underscores the challenges posed by rapid population growth and housing demand in Georgia. Addressing these issues requires comprehensive planning and policies focused on sustainable development, infrastructure enhancement, and environmental preservation.
    """)
