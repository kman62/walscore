import streamlit as st

def calculate_total(accuracy, clarity, customer_focus, business_impact, conciseness, organization, actionability):
    return accuracy + clarity + customer_focus + business_impact + conciseness + organization + actionability

st.title('WAL Scoring Rubric')

st.header('Quality Metrics')
accuracy = st.slider('Accuracy (0-5 points)', min_value=0, max_value=5, value=0)
clarity = st.slider('Clarity (0-5 points)', min_value=0, max_value=5, value=0)
customer_focus = st.slider('Customer Focus (0-5 points)', min_value=0, max_value=5, value=0)
business_impact = st.slider('Business Impact (0-5 points)', min_value=0, max_value=5, value=0)

st.header('Efficiency Metrics')
conciseness = st.slider('Conciseness (0-5 points)', min_value=0, max_value=5, value=0)
organization = st.slider('Organization (0-5 points)', min_value=0, max_value=5, value=0)
actionability = st.slider('Actionability (0-5 points)', min_value=0, max_value=5, value=0)

total_score = calculate_total(accuracy, clarity, customer_focus, business_impact, conciseness, organization, actionability)

st.header(f'Total Score: {total_score} / 35')
