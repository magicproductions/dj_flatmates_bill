from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView
from .forms import BillForm, FlatmateForm, FlatmateBillForm
from .report import PdfReport
from django.templatetags.static import static


class CreateBillView(FormView):
    """Create bill view."""
    template_name = 'home.html'
    form_class = FlatmateBillForm
    
    def post(self, request, *args, **kwargs):
        flatmate_form_1 = FlatmateForm(self.request.POST, prefix='flatmate1')
        flatmate_form_2 = FlatmateForm(self.request.POST, prefix='flatmate2')
        bill_form = BillForm(self.request.POST)
        
        if all([flatmate_form_1.is_valid(), flatmate_form_2.is_valid(), bill_form.is_valid()]):
            flatmate_1 = flatmate_form_1.save()
            flatmate_2 = flatmate_form_2.save()
            bill = bill_form.save()
            
            filename = '_'.join(bill.period.split(' ')) + '.pdf'
            pdf_report = PdfReport(filename)
            pdf_report.generate(flatmate_1, flatmate_2, bill)
            
            pdf_url = static(f'bills/{filename}')
            
            self.request.session['pdf_url'] = pdf_url
            
            return redirect('success')
    
    def form_invalid(self, form):
        return render(
            self.request, self.template_name, {
                'form': form
            }
        )


class SuccessView(View):
    template_name = 'success.html'
    
    def get(self, request, *args, **kwargs):
        pdf_url = request.session.get('pdf_url', '')
        return render(
            request, self.template_name, {
                'pdf_url': pdf_url
            }
        )
