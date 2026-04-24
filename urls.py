from django.urls import path
# from .views import StudentApiView
from .views import StudentView,StudentsView

urlpatterns = [
    # path('students/',StudentApiView.as_view() ),
    path('students/<int:pk>/',StudentView.as_view()),
    path('students/',StudentsView.as_view())
]
