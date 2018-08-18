from django.urls import path
from .views import TweetListView, TweetDetailView, TweetCreateView, TweetUpdateView

urlpatterns = [
	path('', TweetListView.as_view()),
	path('list/<pk>', TweetDetailView.as_view()),
	path('create/', TweetCreateView.as_view()),
	path('update/<pk>/', TweetUpdateView.as_view()),
]