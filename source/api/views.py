from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from homework62.forms import IssueForm
from homework62.models import Issue, Project

from api.serializers import IssueSerializer, ProjectSerializer


class IssueListView(APIView):
    def get(self, request, *args, **kwargs):
        issues = Issue.objects.filter(is_deleted=False)
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data)


class IssueDetailApiView(APIView):
    def get(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        serializer = IssueSerializer(issue)
        return Response(serializer.data)


class IssueUpdateApiView(APIView):
    def put(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        serializer = IssueSerializer(issue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)


class IssueDeleteAPIView(APIView):
    def delete(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        issue.delete()
        serializer = IssueSerializer(issue)
        return Response({"issue_pk": issue.pk})


class ProjectListApiView(APIView):
    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class ProjectDetailApiView(APIView):
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)


class ProjectUpdateApiView(APIView):
    def put(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)


class ProjectDeleteApiView(APIView):
    def delete(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        issues = Issue.objects.filter(project=project)
        for issue in issues:
            issue.project = None
            issue.save()
        project.delete()
        serializer = ProjectSerializer(project)
        return Response({"project_pk": "deleted"})
