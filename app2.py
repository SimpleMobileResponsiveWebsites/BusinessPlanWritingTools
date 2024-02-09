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
    "Input text for designing solutions, products, processes, goods, and services that they would buy, invest, install, or own themselves.")

# New sections based on additional requirements
identifying_goals = st.text_area("Identify your goals")
self_evaluation = st.text_area("Self evaluation")

# Self evaluation checklist - dynamically generated based on the items currently in the application
st.write("## Self Evaluation Checklist")
items = [funding_needs, approach_backers, response_to_yes, legal_details_planning, problem_areas, designing_solutions,
         identifying_goals, self_evaluation]
checklist = st.multiselect("Check the items you've completed:", options=[
    "Funding Needs", "Approach Backers", "Response to Yes", "Legal Details Planning", "Problem Areas",
    "Designing Solutions", "Identifying Goals", "Self Evaluation"
], default=[])

like_business = st.radio("Do you like the business?", ("Yes", "No"))

describe_business = st.text_area("Describe your business")
describe_competitors = st.text_area("Describe your competitor's business")

# Additional text areas for new requirements
taste_trends_technology = st.text_area("Taste, Trends and Technology - How will the future affect your business?")
breakthrough_analysis = st.text_area("Breakthrough Analysis")
breakeven_analysis = st.text_area("Breakeven Analysis")
accomplishments = st.text_area("What Have You Accomplished?")

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

    # New sections based on additional requirements
    st.write("### Identifying Goals")
    st.write(identifying_goals)

    st.write("### Self Evaluation")
    st.write(self_evaluation)

    st.write("### Like the Business")
    st.write(like_business)

    st.write("### Describe the Business")
    st.write(describe_business)

    st.write("### Describe Competitors")
    st.write(describe_competitors)

    st.write("### Taste, Trends, Technology")
    st.write(taste_trends_technology)

    st.write("### Breakthrough Analysis")
    st.write(breakthrough_analysis)

    st.write("### Breakeven Analysis")
    st.write(breakeven_analysis)

    st.write("### Accomplishments")
    st.write(accomplishments)
