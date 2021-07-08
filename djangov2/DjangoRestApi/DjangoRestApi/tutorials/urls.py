from django.urls import path
from django.urls.conf import include
#from tutorials import views
from . import views
from .uapi import UserAPI
#from rest_framework.routers import DefaultRouter
#from .uapi import UserViewSet

#router = DefaultRouter()
#srouter.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('api/tutorials', views.tutorial_list),
    path('api/tutorials/<int:pk>', views.tutorial_detail),
    path('api/tutorials/published', views.tutorial_list_published),
    path('api/login',views.login),
    path('api/newuser', UserAPI.as_view()),
    #path('api/loguser', LogAPI.as_view()),
    #path('api/login', UserViewSet),
    #path('', include(router.urls))
    
]
