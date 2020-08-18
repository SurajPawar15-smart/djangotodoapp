from django.conf.urls import url
from toDoApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.addToDo, name='add'),
    url(r'complete/(?P<todo_id>\d+)$', views.completeToDo, name='complete'),
    url(r'^deletecomplete/$', views.deleteCompleted, name='delcomplete'),
    url(r'^deleteall/$', views.deleteAll, name='delall')

]