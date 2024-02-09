# app1.py
import streamlit as st

# Title of the app
st.title('Business Plan Writing App')

# Select Business Plan Type
business_plan_type = st.selectbox(
    'Choose the type of business plan design:',
    ('Small Business', 'Service Business', 'Manufacturing Business', 'Project Development')
)

# Select Business Plan Duration
business_plan_duration = st.selectbox(
    'Select the duration for the business plan:',
    ('Complete Business Plan', 'One-Day Business Plan', 'Customized Business Plan')
)

# Text input for various sections
funding_needs = st.text_area("How to ask for the money you need")
approach_backers = st.text_area("How to approach different backers")
response_to_yes = st.text_area("What to do when someone says 'yes'")
legal_details_planning = st.text_area("Plan in advance for legal details")

problem_areas = st.text_area("Input text for problem areas and getting out of business")
designing_solutions = st.text_area(
    "Input text for designing solutions, products, processes, goods, and services that they would buy, invest, install, or own themselves."
)

# Submit button
if st.button('Generate Business Plan'):
    st.write("### Business Plan Type")
    st.write(business_plan_type)

    st.write("### Business Plan Duration")
    st.write(business_plan_duration)

    st.write("### Funding Needs")
    st.write(funding_needs)

    st.write("### Approach to Backers")
    st.write(approach_backers)

    st.write("### Response to Yes")
    st.write(response_to_yes)

    st.write("### Legal Details Planning")
    st.write(legal_details_planning)

    st.write("### Problem Areas")
    st.write(problem_areas)

    st.write("### Designing Solutions")
    st.write(designing_solutions)
