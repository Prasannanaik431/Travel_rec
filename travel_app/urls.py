from django.urls import path
from travel_app import views
#TEMPLATE URLS
app_name = 'travel_app'
urlpatterns=[
    path(r'^signup/',views.signup,name='signup'),
    path(r'^user_login/',views.user_login,name='user_login'),
    path(r'^index/',views.index,name='index'),
    path(r'^newq/', views.newq, name='newq'),
    path(r'^destination/',views.destination,name='destination'),
#r'^users/(?P<user_id>\d+)/$'
]
