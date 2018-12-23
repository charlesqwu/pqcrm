from django.urls import path

from . import views

app_name = 'acct'
urlpatterns = [
    path("<str:username>/payments", view=views.payments, name="payments"),
    path("<str:username>/coupons", view=views.coupons, name="coupons"),
    path("<str:username>/transactions", view=views.transactions, name="transactions"),
]
