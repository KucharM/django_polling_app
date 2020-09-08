from django.urls import path
from .views import home, detail, results, vote


app_name = 'polls'

urlpatterns = [
    path('', home, name='home'),
    path('<int:question_id>/', detail, name='detail'),
    path('<int:question_id>/results/', results, name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
]