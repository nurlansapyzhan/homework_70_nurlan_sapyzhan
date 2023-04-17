from django.urls import path

from api.views import IssueListView, IssueDetailApiView, IssueUpdateApiView, IssueDeleteAPIView, ProjectListApiView

urlpatterns = [
    path('issues', IssueListView.as_view(), name='issue_list_view'),
    path('issues/<int:pk>', IssueDetailApiView.as_view(), name='issue_detail_api_view'),
    path('issues/update/<int:pk>', IssueUpdateApiView.as_view(), name='issue_update_api_view'),
    path('issues/delete/<int:pk>', IssueDeleteAPIView.as_view(), name='issue_delete_api_view'),
    path('projects', ProjectListApiView.as_view(), name='project_list_api_view')
]