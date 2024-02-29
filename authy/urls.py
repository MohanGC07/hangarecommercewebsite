from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from authy.views import UserProfile, EditProfile,register,login
# ,accountcreate

urlpatterns = [
    # Profile Section
    path('profileedit/', EditProfile, name="editprofile"),
    path('profile/<str:username>/', views.UserProfile, name='profile'),
    #    path('accounts/', include('allauth.urls')),
     path('users/', include('django.contrib.auth.urls')),
    # User Authentication
    path('sign-up/', views.register, name="sign-up"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout_view, name="logout"),
    # path('accountcreated/', views.accountcreate, name="accountcreate"),
    path('sign-in/', auth_views.LoginView.as_view(template_name="sign-in.html", redirect_authenticated_user=True), name='sign-in'),
    path('sign-out/', auth_views.LogoutView.as_view(template_name="sign-out.html"), name='sign-out'), 
    # Other URLs
    # path('password-reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name='password_reset'),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    # path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name='password_reset_complete'),
]