from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.mi_login, name='login'),
    path('registrar/', views.registrar, name='registrar'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout')
]
