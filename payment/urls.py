from django.contrib import admin
from django.urls import path
from . import views 

app_name ='payment'

urlpatterns=[
      path('makepayment/', views.makepayment, name='make' ),
      path('transaction/verify/<str:ref>/', views.verify_payment, name='verify' ),
      path('initiate/', views.initiate_payment, name='initiate' ),



]