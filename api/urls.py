from django.urls import path
from .views import ImageFilterViews

urlpatterns = [
    path('',ImageFilterViews.as_view()),
]
