from django.urls import path
from .views import home, detail


app_name = 'polls'

urlpatterns = [
    path('', home, name='home'),
    path('<int:question_id>/', detail, name='detail'),
]