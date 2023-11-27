from django.urls import path
from django.urls import re_path as url

from . import views
from .views import BBLoginView, BBLogoutView


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('add_question/', views.addquestion, name='add_question'),
    path('add_choice/', views.addchoice, name='add_choice'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('login/', BBLoginView.as_view(), name='login'),
    path('logout/', BBLogoutView.as_view(), name='logout'),
    path('reg/', views.SignUp.as_view(), name='reg'),
    url(r'^delete/(?P<pk>\d+)$', views.DeleteProfile.as_view(), name='delete'),
    url(r'^update/(?P<pk>\d+)$', views.UpdateProfile.as_view(), name='update'),

]