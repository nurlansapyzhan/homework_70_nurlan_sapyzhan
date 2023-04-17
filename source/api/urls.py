from django.urls import path

from api.views import IssueListView

urlpatterns = [
    path('issues', IssueListView.as_view(), name='issue_list_view')
]