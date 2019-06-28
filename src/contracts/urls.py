from django.urls import path
from contracts import views

urlpatterns = [
    path('', views.ContractListView.as_view()),
    path('<int:pk>/', views.ConctractDetailView.as_view())
]