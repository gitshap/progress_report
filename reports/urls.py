from django.urls import path
from reports.views import home, create_report


urlpatterns = [
    # home page
    path('', home, name='home'),

    # create page
    path('create/', create_report, name='create_report')
]
