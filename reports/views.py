from django.shortcuts import redirect, render

from datetime import date
from reports.models import Report
from reports.forms import ReportForm


def home(request):
    try:
        date_selected = request.POST.get('report-date')
        if not date_selected:
            date_selected = str(date.today())
    except Exception:
        print("eh")
    date_selected_split = date_selected.split("-")
    year = date_selected_split[0]
    month = date_selected_split[1]
    day = date_selected_split[2]
    converted_year = int(year)
    converted_month = int(month)
    converted_day = int(day)
    reports = Report.objects.filter(created_at=date(converted_year,
                                                    converted_month,
                                                    converted_day)).order_by
    ('modified')
    context = {
        'reports': reports
    }
    template_name = 'reports/report_home.html'
    return render(request, template_name=template_name, context=context)


# Create Report
def create_report(request):
    CreateReportForm = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect(home)
    context = {
        'form': CreateReportForm
    }
    template_name = 'reports/report_form.html'
    return render(request, template_name=template_name, context=context)
