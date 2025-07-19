from django.urls import path
from .import views
urlpatterns = [

path("",views.num, name='home1'),

path('article/<int:id>',views.next,name="nextpage"),

path('article/<int:id>/song_file', views.recorder,name='page'),

path('cont', views.contact, name="con"),

path("about", views.about,name="abt"), 

path('help', views.solution,name='help'),

]