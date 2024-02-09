import streamlit as st
from fpdf import FPDF


# Define a function to create a PDF report
def create_pdf_report(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for section, text in content.items():
        pdf.add_page()
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 10, section, 0, 1)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text)

    pdf.output("Business_Plan.pdf")


# Title of the app
st.title('Business Plan Writing App')

# Introduction and Business Concept
st.header('Introduction and Business Concept')
business_plan_type = st.selectbox(
    'Choose the type of business plan design:',
    ('Small Business', 'Service Business', 'Manufacturing Business', 'Project Development')
)
business_plan_duration = st.selectbox(
    'Select the duration for the business plan:',
    ('Complete Business Plan', 'One-Day Business Plan', 'Customized Business Plan')
)
describe_business = st.text_area("Describe your business")
identifying_goals = st.text_area("Identify your goals")
like_business = st.radio("Do you like the business?", ("Yes", "No"))

# Market Analysis
st.header('Market Analysis')
taste_trends_technology = st.text_area("Taste, Trends and Technology - How will the future affect your business?")
describe_competitors = st.text_area("Describe your competitor's business")

# Organization and Management
st.header('Organization and Management')
write_team_plan = st.text_area("Write a Team plan")

# Service or Product Line
st.header('Service or Product Line')
designing_solutions = st.text_area("Designing solutions, products, processes, goods, and services that they would buy, invest, install, or own themselves.")

# Marketing and Sales Strategy
st.header('Marketing and Sales Strategy')
write_marketing_plan = st.text_area("Write a marketing plan")
write_personal_plan = st.text_area("Write a personal plan")

# Funding Request
st.header('Funding Request')
funding_needs = st.text_area("How to ask for the money you need")
potential_money_sources = st.text_area("Potential sources of money to start or expand your small business")
ways_to_raise_money = st.text_area("Ways to Raise Money")
common_money_sources = st.text_area("Common Money Sources to start or expand a business")

# Financial Projections
st.header('Financial Projections')
profit_loss_forecast = st.text_area("Profit and Loss Forecast")
average_cost_of_sales = st.text_area("Determine Average Cost Of Sales")
complete_profit_loss_forecast = st.text_area("Complete A Profit and Loss Forecast")
cash_flow_forecast = st.text_area("Your Cash Flow Forecast and Capital Spending Plan")
required_investment = st.text_area("Required Investment For Your Business")
review_profit_loss_daily = st.text_area("Plan To Review Profit And Loss Daily")

# Appendices
st.header('Appendices')
your_resume = st.text_area("Your Resume")
financial_statement = st.text_area("Your Financial Statement")
credit_reports = st.text_area("Your Experian, Equifax, and Transunion Credit Report")
accomplishment_resume = st.text_area("Accomplishment Resume")
income_tax_return_filings = st.text_area("Your Income Tax Return Filings")

# Other Sections
st.header('Other Sections')
approach_backers = st.text_area("How to approach different backers")
response_to_yes = st.text_area("What to do when someone says 'yes'")
legal_details_planning = st.text_area("Plan in advance for legal details")
problem_areas = st.text_area("Input text for problem areas and getting out of business")
business_financing = st.text_area("Business Financing")
secondary_financing_sources = st.text_area("Secondary sources of financing for start-ups or expansions")
business_plan_summary = st.text_area("Business Plan Summary")
check_for_trouble = st.text_area("Check For Trouble")
self_evaluation = st.text_area("Self evaluation")
accomplishments = st.text_area("What Have You Accomplished?")

# Submit button
if st.button('Generate Business Plan'):
    st.write("### Generated Business Plan Sections")
    # Display all sections in order as per the above organization

# Submit button to generate PDF
if st.button('Generate Business Plan'):
    create_pdf_report(input_data)

    # Providing a download link in Streamlit (works locally)
    with open("Business_Plan.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="Download Business Plan PDF",
                       data=PDFbyte,
                       file_name="Business_Plan.pdf",
                       mime='application/octet-stream')
