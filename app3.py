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

# Existing text inputs
funding_needs = st.text_area("How to ask for the money you need")
approach_backers = st.text_area("How to approach different backers")
response_to_yes = st.text_area("What to do when someone says 'yes'")
legal_details_planning = st.text_area("Plan in advance for legal details")
problem_areas = st.text_area("Input text for problem areas and getting out of business")
designing_solutions = st.text_area(
    "Designing solutions, products, processes, goods, and services that they would buy, invest, install, or own themselves.")

# New text inputs based on previous requirements
identifying_goals = st.text_area("Identify your goals")
self_evaluation = st.text_area("Self evaluation")
like_business = st.radio("Do you like the business?", ("Yes", "No"))
describe_business = st.text_area("Describe your business")
describe_competitors = st.text_area("Describe your competitor's business")
taste_trends_technology = st.text_area("Taste, Trends and Technology - How will the future affect your business?")
breakthrough_analysis = st.text_area("Breakthrough Analysis")
breakeven_analysis = st.text_area("Breakeven Analysis")
accomplishments = st.text_area("What Have You Accomplished?")

# Additional sections for new financial and planning inputs
potential_money_sources = st.text_area("Potential sources of money to start or expand your small business")
ways_to_raise_money = st.text_area("Ways to Raise Money")
common_money_sources = st.text_area("Common Money Sources to start or expand a business")
business_financing = st.text_area("Business Financing")
secondary_financing_sources = st.text_area("Secondary sources of financing for start-ups or expansions")
business_plan_summary = st.text_area("Business Plan Summary")

# Personal and financial information
your_resume = st.text_area("Your Resume")
financial_statement = st.text_area("Your Financial Statement")
credit_reports = st.text_area("Your Experian, Equifax, and Transunion Credit Report")
accomplishment_resume = st.text_area("Accomplishment Resume")
profit_loss_forecast = st.text_area("Profit and Loss Forecast")
average_cost_of_sales = st.text_area("Determine Average Cost Of Sales")
complete_profit_loss_forecast = st.text_area("Complete A Profit and Loss Forecast")
review_profit_loss_daily = st.text_area("Plan To Review Profit And Loss Daily")
income_tax_return_filings = st.text_area("Your Income Tax Return Filings")

# Cash flow and investment
cash_flow_forecast = st.text_area("Your Cash Flow Forecast and Capital Spending Plan")
required_investment = st.text_area("Required Investment For Your Business")

# Trouble checking and planning
check_for_trouble = st.text_area("Check For Trouble")
write_marketing_plan = st.text_area("Write a marketing plan")
write_personal_plan = st.text_area("Write a personal plan")
write_team_plan = st.text_area("Write a Team plan")

# Submit button
if st.button('Generate Business Plan'):
    st.write("### Business Plan Type")
    st.write(business_plan_type)

    st.write("### Business Plan Duration")
    st.write(business_plan_duration)

    # Display existing sections
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

    # Display new sections based on previous and additional requirements
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

    # Display additional financial and planning sections
    st.write("### Potential Money Sources")
    st.write(potential_money_sources)

    st.write("### Ways to Raise Money")
    st.write(ways_to_raise_money)

    st.write("### Common Money Sources")
    st.write(common_money_sources)

    st.write("### Business Financing")
    st.write(business_financing)

    st.write("### Secondary Financing Sources")
    st.write(secondary_financing_sources)

    st.write("### Business Plan Summary")
    st.write(business_plan_summary)

    st.write("### Personal and Financial Information")
    st.write(
        f"Resume: {your_resume}, Financial Statement: {financial_statement}, Credit Reports: {credit_reports}, Accomplishment Resume: {accomplishment_resume}, Profit and Loss Forecast: {profit_loss_forecast}, Average Cost of Sales: {average_cost_of_sales}, Complete Profit and Loss Forecast: {complete_profit_loss_forecast}, Review Profit and Loss Daily: {review_profit_loss_daily}, Income Tax Return Filings: {income_tax_return_filings}")

    st.write("### Cash Flow and Investment")
    st.write(cash_flow_forecast)
    st.write(required_investment)

    st.write("### Planning")
    st.write(check_for_trouble)
    st.write(write_marketing_plan)
    st.write(write_personal_plan)
    st.write(write_team_plan)
