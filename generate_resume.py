import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def create_resume():
    pdf_filename = "Rajresume.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    primary_color = colors.HexColor("#3b82f6")
    text_color = colors.HexColor("#0f172a")
    muted_color = colors.HexColor("#64748b")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=primary_color,
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=text_color,
        spaceAfter=8
    )

    contact_style = ParagraphStyle(
        'ContactInfo',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=muted_color,
        spaceAfter=12
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=primary_color,
        spaceBefore=10,
        spaceAfter=6
    )

    body_bold = ParagraphStyle(
        'BodyBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=text_color
    )

    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=text_color,
        spaceAfter=4
    )

    story = []

    # Header
    story.append(Paragraph("RAJESH GOUDA", title_style))
    story.append(Paragraph("AI & Machine Learning Engineer | B.E. AIML Student", subtitle_style))
    story.append(Paragraph(
        "Email: rajeshpar2005@gmail.com | Phone: +91 8951721253 | Location: Honnavar, Karnataka, India<br/>"
        "LinkedIn: linkedin.com/in/rajesh-gouda038 | GitHub: github.com/rajeshgowda116",
        contact_style
    ))
    story.append(HRFlowable(width="100%", thickness=1, color=primary_color, spaceAfter=10))

    # Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_heading))
    story.append(Paragraph(
        "Passionate Artificial Intelligence & Machine Learning student dedicated to designing intelligent, real-world AI solutions. "
        "Specializes in Machine Learning, Generative AI, RAG architecture, and full-stack AI application development with Python, FastAPI, and Django. "
        "Experienced in hackathons, open-source development, and freelance technical solutions.",
        body_style
    ))

    # Education
    story.append(Paragraph("EDUCATION", section_heading))
    story.append(Paragraph("B.E. in Artificial Intelligence & Machine Learning (2024 – Expected 2028)", body_bold))
    story.append(Paragraph("Yenepoya Institute of Technology (YIT), Moodabidri, Karnataka (Affiliated with VTU Belagavi)", body_style))
    story.append(Paragraph("<i>Focus Areas:</i> Machine Learning, Deep Learning, Data Science, Computer Vision, NLP, Generative AI.", body_style))

    # Experience
    story.append(Paragraph("EXPERIENCE", section_heading))
    story.append(Paragraph("AI & Machine Learning Engineering Student (2025 – Present)", body_bold))
    story.append(Paragraph(
        "• Developed AI chatbots, machine learning predictive models, data analytics dashboards, and web apps with Python, FastAPI, and Scikit-learn.<br/>"
        "• Engineered RAG pipelines and LLM-driven automation tools; active participant in competitive hackathons.",
        body_style
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph("Freelance AI & Python Developer (2026 – Present)", body_bold))
    story.append(Paragraph(
        "• Built custom AI, ML, data analytics, and Python backend solutions for clients including predictive models, REST APIs, and automated tools.",
        body_style
    ))

    # Technical Skills
    story.append(Paragraph("TECHNICAL SKILLS", section_heading))
    skills_data = [
        [Paragraph("<b>Programming:</b>", body_style), Paragraph("Python, SQL, JavaScript, HTML5, CSS3", body_style)],
        [Paragraph("<b>ML & AI:</b>", body_style), Paragraph("Machine Learning, Deep Learning, Scikit-learn, TensorFlow, PyTorch, CV, NLP, GenAI, RAG, LLMs", body_style)],
        [Paragraph("<b>Backend & DB:</b>", body_style), Paragraph("FastAPI, Django, Flask, REST APIs, MySQL, SQLite, MongoDB", body_style)],
        [Paragraph("<b>Tools & Cloud:</b>", body_style), Paragraph("Git, GitHub, Docker, VS Code, Jupyter, Google Colab, Vercel, Render, Hugging Face Spaces", body_style)]
    ]
    t = Table(skills_data, colWidths=[110, 420])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t)

    # Key Projects
    story.append(Paragraph("KEY PROJECTS", section_heading))
    story.append(Paragraph("1. EduLink – Smart College Management Platform", body_bold))
    story.append(Paragraph("Full-stack college platform with role-based dashboards for admins, faculty, advisors, and students. Attendance, study materials, announcements, performance tracking. Built with Python, Django, HTML5, CSS3, JavaScript, SQLite/MySQL.", body_style))
    
    story.append(Paragraph("2. AI Math Chat – Conversational Math Assistant", body_bold))
    story.append(Paragraph("Conversational assistant providing step-by-step math explanations with real-time streaming responses and session history. Built with Python, FastAPI, OpenAI API, SQLite, JavaScript.", body_style))

    story.append(Paragraph("3. Student Mail Agent – Autonomous AI Email Assistant", body_bold))
    story.append(Paragraph("Smart AI email assistant for students featuring summary generation, priority detection, draft replies, and deadline extraction via Gmail API & LLMs.", body_style))

    # Certifications & Achievements
    story.append(Paragraph("CERTIFICATIONS & ACHIEVEMENTS", section_heading))
    certs = [
        "• <b>GenAI Powered Data Analytics Job Simulation</b> – Tata Group × Forage (Jun 2026)",
        "• <b>Git Training Certification</b> – IIT Bombay (86.67% score, Dec 2025)",
        "• <b>R Programming Training Certification</b> – IIT Bombay (82.50% score, May 2026)",
        "• <b>Python Pandas Course</b> – Intellipaat Academy (Feb 2026)",
        "• <b>Hackathon Participant</b> – Open Loop 2026 (Team Yen Quads, Yenepoya School of Engineering)"
    ]
    for cert in certs:
        story.append(Paragraph(cert, body_style))

    doc.build(story)
    print(f"Successfully generated {pdf_filename}")

if __name__ == "__main__":
    create_resume()
