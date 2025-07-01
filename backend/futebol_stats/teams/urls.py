from django.urls import path
from .views import TeamDetailView

urlpatterns = [
    path('<int:team_id>/', TeamDetailView.as_view(), name='team-detail'),
]