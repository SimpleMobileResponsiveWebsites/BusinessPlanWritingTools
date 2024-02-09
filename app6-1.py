import streamlit as st
from fpdf import FPDF


# Define the function to create a PDF report
def create_pdf_report(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for section, text in content.items():
        pdf.add_page()  # Ensure each section starts on a new page for clarity
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 10, section, 0, 1)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text.strip())
        pdf.ln(10)  # Add a line break between sections for better readability

    pdf.output("Business_Plan.pdf")


# Initialize an empty dictionary to store user inputs for PDF generation
input_data = {}

# Title of the Streamlit app
st.title('Business Plan Writing App')


# Function to display input widgets and collect user responses
def collect_inputs():
    # Introduction and Business Concept
    st.header('Introduction and Business Concept')
    business_plan_type = st.selectbox('Choose the type of business plan design:',
                                      ('Small Business', 'Service Business', 'Manufacturing Business',
                                       'Project Development'),
                                      key='business_plan_type')
    business_plan_duration = st.selectbox('Select the duration for the business plan:',
                                          ('Complete Business Plan', 'One-Day Business Plan',
                                           'Customized Business Plan'),
                                          key='business_plan_duration')
    describe_business = st.text_area("Describe your business", key='describe_business')
    identifying_goals = st.text_area("Identify your goals", key='identifying_goals')
    like_business = st.radio("Do you like the business?", ("Yes", "No"), key='like_business')

    # Add responses to input_data dictionary
    input_data['Introduction and Business Concept'] = f"""Business Plan Type: {business_plan_type}
Business Plan Duration: {business_plan_duration}
Describe your business: {describe_business}
Identify your goals: {identifying_goals}
Do you like the business? {like_business}
"""

    # Market Analysis
    st.header('Market Analysis')
    taste_trends_technology = st.text_area("Taste, Trends and Technology - How will the future affect your business?",
                                           key='taste_trends_technology')
    describe_competitors = st.text_area("Describe your competitor's business", key='describe_competitors')
    input_data['Market Analysis'] = f"""Taste, Trends and Technology: {taste_trends_technology}
Describe Competitors: {describe_competitors}
"""

    # Repeat this structure for other sections...

    # Organization and Management
    st.header('Organization and Management')
    write_team_plan = st.text_area("Write a Team plan", key='write_team_plan')
    input_data['Organization and Management'] = f"Team Plan: {write_team_plan}\n"

    # Additional sections should follow the same pattern

    # Example for Service or Product Line (ensure to repeat for all sections)
    st.header('Service or Product Line')
    designing_solutions = st.text_area(
        "Designing solutions, products, processes, goods, and services that they would buy, invest, install, or own themselves.",
        key='designing_solutions')
    input_data['Service or Product Line'] = f"Designing Solutions: {designing_solutions}\n"

    # Make sure to capture all sections as per app5.py structure


# Collect user inputs
collect_inputs()

# Button to generate and download the PDF
if st.button('Generate Business Plan', key='generate_pdf'):
    create_pdf_report(input_data)

    # Read the generated PDF for download
    with open("Business_Plan.podf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="Download Business Plan PDF",
                       data=PDFbyte,
                       file_name="Business_Plan.pdf",
                       mime='application/octet-stream')
