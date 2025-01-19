from django.urls import path, include

urlpatterns = [
    # Include routes from health_controller
    path('health/', include('users.controllers.health_controller')),

    # Include routes from user_controller
    path('users/', include('users.controllers.user_controller')),

    path('greet_user/<str:user_id>/', include('users.controllers.greet_controller'))
]
