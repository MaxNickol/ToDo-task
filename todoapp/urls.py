from django.urls import path
from .views import home_page, create_todo, todo_delete

urlpatterns =[
    path('', home_page, name='home_page'),
    path('create', create_todo, name='create_todo'),
    path('<int:todo_id>/delete', todo_delete, name='todo_delete')
]