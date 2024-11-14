from django.urls import path
from . import views


urlpatterns = [
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('login',views.login_users,name='login'),
    path('logout',views.logout_users,name='logout'),
    path('register',views.register_users,name='register'),
    path('product/<int:pk>',views.product,name='product'),
    path('getcategory/<id>',views.getcategory,name='getcategory/<id>'),
   
]