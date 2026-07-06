from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        pass

    def footer(self):
        pass

def create_resume():
    pdf = PDF(format='A4')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Fonts
    # Arial/Helvetica is standard for ATS
    pdf.set_font('Helvetica', 'B', 18)
    
    # Name
    pdf.cell(0, 8, 'SUDIP KUMAR ADAK', ln=True, align='C')
    
    # Contact Info
    pdf.set_font('Helvetica', '', 10)
    contact_info = "Pune, Maharashtra, India | adaksudip956@gmail.com | LinkedIn: sudip-kumar-adak-26b303245"
    pdf.cell(0, 5, contact_info, ln=True, align='C')
    contact_info_2 = "GitHub: Thebright10 | Portfolio: thebright10.github.io/Portfolio_Sudip/"
    pdf.cell(0, 5, contact_info_2, ln=True, align='C')
    
    pdf.ln(5)
    
    # --- SUMMARY ---
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 6, 'PROFESSIONAL SUMMARY', ln=True, border='B')
    pdf.ln(2)
    pdf.set_font('Helvetica', '', 11)
    summary = (
        "Motivated Software Developer and MCA student with a strong foundation in AI/ML, web development "
        "(frontend and backend), and data analytics. Proven ability to build impactful applications like AI "
        "mental health platforms and e-commerce systems. Seeking internship and full-time opportunities "
        "to leverage technical skills in a dynamic IT environment."
    )
    pdf.multi_cell(0, 5, summary)
    pdf.ln(5)
    
    # --- EDUCATION ---
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 6, 'EDUCATION', ln=True, border='B')
    pdf.ln(2)
    
    # MCA
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(140, 5, 'Master of Computer Applications (MCA)', ln=0)
    pdf.set_font('Helvetica', '', 11)
    pdf.cell(0, 5, '2024 - Present', ln=1, align='R')
    pdf.set_font('Helvetica', 'I', 11)
    pdf.cell(0, 5, 'Pimpri Chinchwad University (PCU), Pune, India', ln=1)
    pdf.ln(2)
    
    # BCA
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(140, 5, 'Bachelor of Computer Applications (BCA)', ln=0)
    pdf.set_font('Helvetica', '', 11)
    pdf.cell(0, 5, '2021 - 2024', ln=1, align='R')
    pdf.set_font('Helvetica', 'I', 11)
    pdf.cell(0, 5, 'Techno India Institute of Technology, Kolkata, West Bengal', ln=1)
    pdf.ln(2)
    
    # Class XII
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(140, 5, 'Class XII (Higher Secondary)', ln=0)
    pdf.set_font('Helvetica', '', 11)
    pdf.cell(0, 5, '2021 - 2022', ln=1, align='R')
    pdf.set_font('Helvetica', 'I', 11)
    pdf.cell(0, 5, 'Santragachi Kedarnath Institution, West Bengal', ln=1)
    pdf.set_font('Helvetica', '', 11)
    pdf.cell(0, 5, 'Marks: 81.4%', ln=1)
    pdf.ln(5)
    
    # --- TECHNICAL SKILLS ---
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 6, 'TECHNICAL SKILLS', ln=True, border='B')
    pdf.ln(2)
    
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(40, 5, 'Programming:', ln=0)
    pdf.set_font('Helvetica', '', 11)
    pdf.cell(0, 5, 'Python, Java, C, SQL', ln=1)
    
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(40, 5, 'Web Dev:', ln=0)
    pdf.set_font('Helvetica', '', 11)
    pdf.cell(0, 5, 'HTML, CSS, JavaScript, Django', ln=1)
    
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(40, 5, 'AI & Data:', ln=0)
    pdf.set_font('Helvetica', '', 11)
    pdf.cell(0, 5, 'Machine Learning, NLP, Data Analytics, Matplotlib', ln=1)
    
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(40, 5, 'Tools:', ln=0)
    pdf.set_font('Helvetica', '', 11)
    pdf.cell(0, 5, 'Git, GitHub, VS Code, REST APIs', ln=1)
    pdf.ln(5)
    
    # --- PROJECTS ---
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 6, 'PROJECTS', ln=True, border='B')
    pdf.ln(2)
    
    # Project 1
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 5, 'MindFlow AI - Mental Health Platform', ln=1)
    pdf.set_font('Helvetica', 'I', 11)
    pdf.cell(0, 5, 'Full-Stack Developer & ML Engineer (Python, Django, NLP)', ln=1)
    pdf.set_font('Helvetica', '', 11)
    pdf.multi_cell(0, 5, '- Developed a comprehensive AI-powered mental health support platform.\n- Implemented real-time emotion detection using Natural Language Processing (NLP).\n- Built an empathetic AI support chatbot and emotional wellness tracking dashboard.')
    pdf.ln(3)
    
    # Project 2
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 5, 'Grilli - Restaurant Table Booking System', ln=1)
    pdf.set_font('Helvetica', 'I', 11)
    pdf.cell(0, 5, 'Frontend Developer (HTML, CSS, JavaScript)', ln=1)
    pdf.set_font('Helvetica', '', 11)
    pdf.multi_cell(0, 5, '- Designed a luxurious, dark-themed restaurant website with an elegant table booking system.\n- Created interactive reservation forms and a secure, responsive login portal.\n- Focused on premium UI/UX design to enhance customer engagement.')
    pdf.ln(3)
    
    # Project 3
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 5, 'E-Commerce Platform', ln=1)
    pdf.set_font('Helvetica', 'I', 11)
    pdf.cell(0, 5, 'Web Developer (HTML, CSS, JavaScript)', ln=1)
    pdf.set_font('Helvetica', '', 11)
    pdf.multi_cell(0, 5, '- Built a full-featured e-commerce web application with dynamic product catalogs.\n- Implemented shopping cart functionality and user authentication flows.\n- Ensured a fully responsive design for seamless mobile and desktop shopping experiences.')
    pdf.ln(3)
    
    # Project 4
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 5, 'Data Analytics Dashboard', ln=1)
    pdf.set_font('Helvetica', 'I', 11)
    pdf.cell(0, 5, 'Data Analyst (Python, Matplotlib)', ln=1)
    pdf.set_font('Helvetica', '', 11)
    pdf.multi_cell(0, 5, '- Created an interactive data analytics and visualization dashboard using Python.\n- Designed dynamic charts and KPI metrics to provide insightful data-driven reports.')
    
    pdf.output('Sudip_Kumar_Adak_Resume.pdf')
    print("Resume PDF generated successfully.")

if __name__ == '__main__':
    create_resume()
