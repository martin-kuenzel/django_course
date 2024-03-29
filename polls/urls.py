from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(), name='poll_index'),

    path('<int:pk>/details/', views.DetailView.as_view(), name='poll_details'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='poll_results'),
    path('<int:pk>/', views.ResultsView.as_view(), name='poll_results'),

    path('<int:poll_id>/vote/', views.poll_vote, name='poll_vote'),

    path('poll_create/',views.PollCreateView.as_view(), name = 'poll_create'),
    path('poll_create_done/', views.save_poll, name = 'poll_create_done')
]