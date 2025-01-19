from django.urls import path
from ..views.greet_view import GreetView

urlpatterns = [
    path('', GreetView.as_view(), name='greet_user'),  # POST: Create user
]