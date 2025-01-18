from flask import Flask, render_template, request, send_file
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Collect data from the form
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        address = request.form.get('address', '').strip()
        linkedin = request.form.get('linkedin', '').strip()
        portfolio = request.form.get('portfolio', '').strip()
        dob = request.form.get('dob', '').strip()
        education = request.form.get('education', '').strip()
        experience = request.form.get('experience', '').strip()
        skills = request.form.get('skills', '').strip()
        projects = request.form.get('projects', '').strip()
        languages = request.form.get('languages', '').strip()
        certifications = request.form.get('certifications', '').strip()

        # Validate required fields
        if not name:
            return "Error: Name is required.", 400

        # Generate the CV PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)

        # Set font and colors
        pdf.set_font('Arial', 'B', 24)
        pdf.set_text_color(0, 0, 0)  # Black text
        pdf.set_fill_color(200, 220, 255)  # Light blue background for header

        # Title
        pdf.cell(0, 15, 'Curriculum Vitae', ln=True, align='C', fill=True)
        pdf.ln(10)

        # Personal Details Section
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, 'Personal Information', ln=True)
        pdf.set_font('Arial', '', 12)
        pdf.cell(0, 8, f'Name: {name}', ln=True)
        if email: pdf.cell(0, 8, f'Email: {email}', ln=True)
        if phone: pdf.cell(0, 8, f'Phone: {phone}', ln=True)
        if address: pdf.cell(0, 8, f'Address: {address}', ln=True)
        pdf.ln(10)

        # Links Section
        if linkedin or portfolio:
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(0, 10, 'Links', ln=True)
            pdf.set_font('Arial', '', 12)
            if linkedin: pdf.cell(0, 8, f'LinkedIn: {linkedin}', ln=True)
            if portfolio: pdf.cell(0, 8, f'Portfolio: {portfolio}', ln=True)
            pdf.ln(10)

        # Date of Birth
        if dob:
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(0, 10, 'Date of Birth', ln=True)
            pdf.set_font('Arial', '', 12)
            pdf.cell(0, 8, dob, ln=True)
            pdf.ln(10)

        # Education Section
        if education:
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(0, 10, 'Education', ln=True)
            pdf.set_font('Arial', '', 12)
            pdf.multi_cell(0, 8, education)
            pdf.ln(10)

        # Work Experience Section
        if experience:
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(0, 10, 'Work Experience', ln=True)
            pdf.set_font('Arial', '', 12)
            pdf.multi_cell(0, 8, experience)
            pdf.ln(10)

        # Skills Section
        if skills:
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(0, 10, 'Skills', ln=True)
            pdf.set_font('Arial', '', 12)
            pdf.multi_cell(0, 8, skills)
            pdf.ln(10)

        # Projects Section
        if projects:
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(0, 10, 'Projects', ln=True)
            pdf.set_font('Arial', '', 12)
            pdf.multi_cell(0, 8, projects)
            pdf.ln(10)

        # Languages Section
        if languages:
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(0, 10, 'Languages', ln=True)
            pdf.set_font('Arial', '', 12)
            pdf.multi_cell(0, 8, languages)
            pdf.ln(10)

        # Certifications Section
        if certifications:
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(0, 10, 'Certifications and Awards', ln=True)
            pdf.set_font('Arial', '', 12)
            pdf.multi_cell(0, 8, certifications)
            pdf.ln(10)

        # Save the PDF to a file
        pdf_file = f"{name.replace(' ', '_')}_CV.pdf"
        pdf.output(pdf_file)

        # Send the PDF file for download
        return send_file(pdf_file, as_attachment=True, download_name=pdf_file)

    except Exception as e:
        # Handle any unexpected errors
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)