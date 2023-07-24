from django.urls import path

from core.views import CreateBillView, SuccessView

urlpatterns = [
    path('home', CreateBillView.as_view(), name='home'),
    path('success', SuccessView.as_view(), name='success'),
]
