from django.urls import path
from .views import CreateImageView, ListImageView


urlpatterns = [
    path('create/', CreateImageView.as_view()),
    path('list/', ListImageView.as_view()),
]