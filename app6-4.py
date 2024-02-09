import streamlit as st
from fpdf import FPDF


# Define a function to create a PDF report
def create_pdf_report(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)  # Ensure the font color is set to black

    for section, text in content.items():
        pdf.add_page()  # Start each section on a new page for clarity
        pdf.set_font("Arial", 'B', size=16)
        pdf.cell(0, 10, section, 0, 1, 'C')  # Add section title
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text)  # Add section text
        pdf.ln(10)  # Add a line break between sections

    pdf_file_path = "Business_Plan.pdf"
    pdf.output(pdf_file_path)
    return pdf_file_path


# Initialize an empty dictionary to store user inputs for PDF generation
input_data = {}

# Title of the Streamlit app
st.title('Business Plan Writing App')

# Collect inputs for all sections of the business plan
sections = {
    'Introduction and Business Concept': [
        'Describe your business',
        'Identify your goals',
        'Do you like the business? Yes/No'
    ],
    'Market Analysis': [
        'Taste, Trends and Technology - How will the future affect your business?',
        'Describe your competitor\'s business'
    ],
    'Marketing and Sales Strategy': [
        'Write a marketing plan',
        'Write a personal plan'
    ],
    'Funding Request': [
        'How to ask for the money you need',
        'Potential sources of money to start or expand your small business',
        'Ways to Raise Money',
        'Common Money Sources to start or expand a business'
    ],
    'Financial Projections': [
        'Profit and Loss Forecast',
        'Determine Average Cost Of Sales',
        'Complete A Profit and Loss Forecast',
        'Your Cash Flow Forecast and Capital Spending Plan',
        'Required Investment For Your Business'
    ]
}

for section, prompts in sections.items():
    st.header(section)
    responses = []
    for prompt in prompts:
        if "Yes/No" in prompt:
            response = st.radio(prompt.split(" Yes/No")[0], ["Yes", "No"], key=prompt)
        else:
            response = st.text_area(prompt, key=prompt)
        responses.append(f"{prompt}: {response}")
    input_data[section] = "\n".join(responses)

# Generate and download the PDF
if st.button('Generate Business Plan', key='generate_pdf'):
    pdf_file_path = create_pdf_report(input_data)

    with open(pdf_file_path, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="Download Business Plan PDF",
                       data=PDFbyte,
                       file_name="Business_Plan.pdf",
                       mime='application/pdf')  # Correct MIME type for PDF
