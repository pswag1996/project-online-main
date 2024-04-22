from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
    path('main', views.home, name='home'),
    path('project_teacher', views.project_t, name='project_teacher'),
    path('project_year', views.project_y, name='project_year'),
    path('project_software', views.project_s, name='project_software'),
    path('project_hardware', views.project_h, name='project_hardware'),
    path('profile', views.profile, name='profile'),
    path('save_profile', views.profile_save, name='profile_save'),
    path('viewproject', views.view_project, name='view_project'),
    path('newproject', views.new_project, name='new_project'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)