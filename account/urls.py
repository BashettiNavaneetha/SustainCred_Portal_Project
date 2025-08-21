
# from . import views

# from django_distill import distill_url
# def get_none():
#     return None

# urlpatterns = [
    
#     distill_url('', views.home, name='home'),
#     distill_url('register/', views.register, name='register'),
#     distill_url('login/', views.user_login, name='login'),
#     distill_url('upload_resume/', views.upload_resume, name='upload_resume'),
#     distill_url('delete_resume/', views.delete_resume, name='delete_resume'),
#     distill_url('logout/',views.user_logout,name='logout'),
# ]

from django_distill import distill_path
from . import views

def get_none():
    return None

urlpatterns = [
    distill_path('', views.home, name='home', distill_func=get_none),
    distill_path('register/', views.register, name='register', distill_func=get_none),
    distill_path('login/', views.user_login, name='login', distill_func=get_none),
    distill_path('upload_resume/',views.upload_resume,name='upload_resume', distill_func=get_none),
    distill_path('logout/',views.logout,name='logout', distill_func=get_none),
]
