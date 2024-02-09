import streamlit as st
from fpdf import FPDF


# Define a function to create a PDF report
def create_pdf_report(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)#Ensure the font color is set to black


    for section, text in content.items():
        pdf.add_page()  # Start each section on a new page for clarity
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 10, section, 0, 1)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text.strip())
        pdf.ln(10)  # Add a line break between sections

    pdf.output("Business_Plan.pdf")


# Initialize an empty dictionary to store user inputs for PDF generation
input_data = {}

# Title of the Streamlit app
st.title('Business Plan Writing App')

# Collect inputs for all sections of the business plan
# Introduction and Business Concept
st.header('Introduction and Business Concept')
business_plan_type = st.selectbox(
    'Choose the type of business plan design:',
    ('Small Business', 'Service Business', 'Manufacturing Business', 'Project Development'),
    key='business_plan_type'
)
business_plan_duration = st.selectbox(
    'Select the duration for the business plan:',
    ('Complete Business Plan', 'One-Day Business Plan', 'Customized Business Plan'),
    key='business_plan_duration'
)
describe_business = st.text_area("Describe your business", key='describe_business')
identifying_goals = st.text_area("Identify your goals", key='identifying_goals')
like_business = st.radio("Do you like the business?", ("Yes", "No"), key='like_business')

input_data['Introduction and Business Concept'] = "\n".join([
    f"Business Plan Type: {business_plan_type}",
    f"Business Plan Duration: {business_plan_duration}",
    f"Describe your business: {describe_business}",
    f"Identify your goals: {identifying_goals}",
    f"Do you like the business? {like_business}"
])

# Market Analysis
st.header('Market Analysis')
taste_trends_technology = st.text_area("Taste, Trends and Technology - How will the future affect your business?",
                                       key='taste_trends_technology')
describe_competitors = st.text_area("Describe your competitor's business", key='describe_competitors')

input_data['Market Analysis'] = "\n".join([
    f"Taste, Trends and Technology: {taste_trends_technology}",
    f"Describe Competitors: {describe_competitors}"
])

# Marketing and Sales Strategy
st.header('Marketing and Sales Strategy')
write_marketing_plan = st.text_area("Write a marketing plan", key='write_marketing_plan')
write_personal_plan = st.text_area("Write a personal plan", key='write_personal_plan')

input_data['Marketing and Sales Strategy'] = "\n".join([
    f"Marketing Plan: {write_marketing_plan}",
    f"Personal Plan: {write_personal_plan}"
])

# Funding Request
st.header('Funding Request')
funding_needs = st.text_area("How to ask for the money you need", key='funding_needs')
potential_money_sources = st.text_area("Potential sources of money to start or expand your small business",
                                       key='potential_money_sources')
ways_to_raise_money = st.text_area("Ways to Raise Money", key='ways_to_raise_money')
common_money_sources = st.text_area("Common Money Sources to start or expand a business", key='common_money_sources')

input_data['Funding Request'] = "\n".join([
    f"How to ask for the money you need: {funding_needs}",
    f"Potential sources of money: {potential_money_sources}",
    f"Ways to Raise Money: {ways_to_raise_money}",
    f"Common Money Sources: {common_money_sources}"
])

# Financial Projections
st.header('Financial Projections')
profit_loss_forecast = st.text_area("Profit and Loss Forecast", key='profit_loss_forecast')
average_cost_of_sales = st.text_area("Determine Average Cost Of Sales", key='average_cost_of_sales')
complete_profit_loss_forecast = st.text_area("Complete A Profit and Loss Forecast", key='complete_profit_loss_forecast')
cash_flow_forecast = st.text_area("Your Cash Flow Forecast and Capital Spending Plan", key='cash_flow_forecast')
required_investment = st.text_area("Required Investment For Your Business", key='required_investment')

input_data['Financial Projections'] = "\n".join([
    f"Profit and Loss Forecast: {profit_loss_forecast}",
    f"Average Cost Of Sales: {average_cost_of_sales}",
    f"Complete A Profit and Loss Forecast: {complete_profit_loss_forecast}",
    f"Cash Flow Forecast and Capital Spending Plan: {cash_flow_forecast}",
    f"Required Investment For Your Business: {required_investment}"
])

# Appendices and Other Sections as per the original instructions can be added similarly

# Generate and download the PDF
if st.button('Generate Business Plan', key='generate_pdf'):
    create_pdf_report(input_data)

    with open("Business_Plan.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="Download Business Plan PDF",
                       data=PDFbyte,
                       file_name="Business_Plan.pdf",
                       mime='application/octet-stream')
