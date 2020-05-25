from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('booking', views.booking, name="booking"),
    path('booknow/<int:pk>/', views.booknow, name="booknow"),
    path('cancel', views.cancel, name="cancel"),
    path('mybooking',views.mybooking,name="mybooking"),
    url(r'^edit/(?P<pk>\d+)/$' , views.edit, name = 'edit'),
    url(r'^delete/(?P<pk>\d+)/$' , views.delete, name = 'delete'),
    path('payment', views.payment, name="payment"),
    path('search', views.search, name="search"),
    
]
