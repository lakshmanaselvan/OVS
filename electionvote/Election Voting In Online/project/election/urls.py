from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('voting/',views.voting_page,name="voting_page"),
    path('register/',views.register,name="register"),
    path('votecount/',views.vote_count,name="vote_count")
]