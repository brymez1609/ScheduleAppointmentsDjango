from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from Appointments import settings
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list_patients, name='list_patients'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),

    #API VIEWS
    path('list_api/', views.ListUsersApiView.as_view(), name='list_patients_api'),    
]