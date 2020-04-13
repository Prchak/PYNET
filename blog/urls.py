from django.urls import path
from . import views

#app_name = 'blog'

urlpatterns = [
    path('', views.home, name = 'pynet-home'),
    path('about/', views.about, name = 'pynet-about'),
    path('contactus/',views.contactform, name='pynet-contactus'),
    #path('redirect/',views.contactform),
    path('success/',views.success, name='success')
]