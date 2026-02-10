from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from authy.views import UserProfile, EditProfile, register


urlpatterns = [
    # Profile Section
    path('profileedit/', EditProfile, name="editprofile"),
    path('profile/<str:username>/', views.UserProfile, name='profile'),
    path('users/', include('django.contrib.auth.urls')),

    # User Authentication
    path('sign-up/', views.register, name="sign-up"),
    # path('sign-in/', views.login, name="sign-in"),
    # path('login/', views.login_redirect, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('sign-in/', auth_views.LoginView.as_view(template_name="sign-in.html", redirect_authenticated_user=True), name='sign-in'),
    path('sign-out/', auth_views.LogoutView.as_view(template_name="sign-out.html"), name='sign-out'), 
]
    