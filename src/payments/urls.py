from django.urls import path
from payments import views


urlpatterns = [
    path('<int:contract_id>/', views.PaymentCreate.as_view())
]