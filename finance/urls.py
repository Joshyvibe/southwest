from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = 'finance'

urlpatterns = [
    path('transfer/success/', views.success, name='success'),
    path('transfer_form/', views.transfer_form, name='transfer_form'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]


urlpatterns += staticfiles_urlpatterns()