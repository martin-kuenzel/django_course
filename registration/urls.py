from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    # Der Password renewal process läuft in der gegebenen Reihenfolge ab
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),

    #TODO
    # path('create-user/',views.UserCreationFormView.as_view(),'user_create')
    #path('profile/<int:pk>',views.ProfileView.as_view(),name='user_profile')
]