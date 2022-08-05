from django.urls import path, include
from django.views import generic

from . import views


urlpatterns = [
    path('', generic.RedirectView.as_view(url='./sample/'), name="index"),
    path('sample/', include(views.SampleViewSet().urls)),
]
