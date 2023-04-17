from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from homework62.forms import IssueForm
from homework62.models import Issue

from api.serializers import IssueSerializer


class IssueListView(APIView):
    def get(self, request, *args, **kwargs):
        issues = Issue.objects.filter(is_deleted=False)
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data)


