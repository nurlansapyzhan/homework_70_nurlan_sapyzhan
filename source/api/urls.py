from django.urls import path

from api.views import IssueListView, IssueDetailApiView, IssueUpdateApiView

urlpatterns = [
    path('issues', IssueListView.as_view(), name='issue_list_view'),
    path('issues/<int:pk>', IssueDetailApiView.as_view(), name='issue_detail_api_view'),
    path('issues/update/<int:pk>', IssueUpdateApiView.as_view(), name='issue_update_api_view')
]