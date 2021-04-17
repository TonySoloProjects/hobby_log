# learning_logs\urls.py

from django.urls import path, include
from . import views

app_name = 'hobby'
urlpatterns = [
    # Home page
    path('', views.index, name='view_index'),
    path('topics/', views.view_topics, name='view_topics'),
    path('topic/<int:topic_id>', views.view_topic, name='view_topic'),
    path('topic/<int:topic_id>/delete/', views.delete_topic, name='delete_topic'),
    path('create_topic/', views.create_topic, name='create_topic'),
    path('create_entry/', views.create_entry, name='create_entry'),
    path('create_entry/<int:topic_id>', views.create_entry, name='create_entry_with_id'),
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]
