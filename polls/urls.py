from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='polls-index'),
    path('polls/details/<int:id>/', views.poll_details, name='poll-details')
]