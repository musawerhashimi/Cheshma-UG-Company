from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('news/<int:pk>/',news_details,name='news-details'),
    path('product/<int:pk>/',product_details,name='product-details'),
    path('contact',user_contact,name='contact'),
    path('login',login_user,name='login'),
    path('logout',logout_user,name='logout'),
    path('reset_password',password_reset,name='reset_password'),
    path('imprint',imprint,name='imprint'),

]