from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),             # Home page
    path('topics/', views.topics, name='topics'),    # Show all topics
    path('topics/<int:topic_id>/', views.topic, name='topic'),  # A single topic
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),  # Add new entry
]

