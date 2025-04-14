from django.urls import path
from . import views

urlpatterns = [
    # Route to list all RSS feeds or add a new one
    path('feeds/', views.FeedListCreateAPIView.as_view()),
    # Route to retrieve, update or delete a specific feed via its ID    
    path('feeds/<int:pk>/', views.FeedDetailAPIView.as_view()),
    # Route to get all articles linked to a specific feed
    path('feeds/<int:pk>/items/', views.FeedItemsAPIView.as_view()),
]
