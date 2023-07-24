import os

from django.conf import settings
from fpdf import FPDF


class PdfReport:
    """Creates a pdf file that contains the details of the flatmates and the amount they have to pay."""
    
    def __init__(self, filename):
        self.filename = filename
    
    def generate(self, flatmate1, flatmate2, bill):
        flatmate_1_pay = flatmate1.pays(bill, flatmate2)
        flatmate_2_pay = flatmate2.pays(bill, flatmate1)
        
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()
        
        # Add icon
        if settings.DEBUG:
            image_path = os.path.join(settings.STATICFILES_DIRS[0], 'images/house.png')
        else:
            image_path = os.path.join(settings.STATIC_ROOT, 'images/house.png')
        pdf.image(image_path, w=30, h=30)
        
        # Insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)
        
        # Insert period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)
        
        # Insert name and amount of the first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=f'£{flatmate_1_pay}', border=0, ln=1)
        
        # Insert name and amount of the second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=f'£{flatmate_2_pay}', border=0, ln=1)
        
        #  Create bills directory if it doesn't exist.
        os.makedirs('core/static/bills', exist_ok=True)
        
        # Save the pdf file in the bills directory
        pdf.output(os.path.join('core/static/bills', self.filename))
