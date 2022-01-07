from django.forms import ModelForm

from reports.models import Report


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = '__all__'