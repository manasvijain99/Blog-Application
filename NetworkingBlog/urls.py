from Blog import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.user_signup,name='signup'),
    path('logout/',views.user_logout,name='logout'),
    path('addpost/',views.add_post,name='addpost'), #these are dynamic urls that is why we have added a pk because every time vlaue changes
    path('updatepost/<int:id>/',views.update_post,name='updatepost'),
    path('deletepost/<int:id>/',views.delete_post,name='deletepost')



]
