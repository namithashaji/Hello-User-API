from django.urls import path
from ..views.user_views import UserViews

urlpatterns = [
    path('', UserViews.as_view(), name='create_user'),  # POST: Create user
    path('<int:user_id>/', UserViews.as_view(), name='user_detail'),  # GET/PUT/DELETE: User operations
]
