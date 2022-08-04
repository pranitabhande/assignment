from django.urls import path,include
from assignment_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('postcommentdata',views.postcommentdata,name='postcommentdata'),
    path('submitblog',views.submitblog,name='submitblog'),
    path('upvote',views.upvote,name='upvote'),
    path('downvote',views.downvote,name='downvote'),
    path('blog/<str:pk>',views.blog,name='blog'),
    path('login',views.reqlogin,name='login'),
    path('logout',views.reqlogout,name='logout'),
    path('register',views.register,name='register'),
    path('getdata',views.getdata,name='getdata'),
    path('postdata',views.postdata,name='postdata'),
    
    path('putdata/<str:pk>',views.putdata,name='putdata'),

    
    
    
    
    
]