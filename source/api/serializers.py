from django.contrib.auth.models import User
from rest_framework import serializers

from homework62.models import Issue, Status, Type, Project


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ProjectSerializer(serializers.ModelSerializer):
    members = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = ('id', 'start_date', 'end_date', 'name', 'description', 'members')
        read_only_fields = ('id', 'members')


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name')
        read_only_fields = ('id',)


class IssueSerializer(serializers.ModelSerializer):
    status = serializers.PrimaryKeyRelatedField(read_only=True)
    type = TypeSerializer(read_only=True, many=True)
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Issue
        fields = (
            'id', 'summary', 'description', 'status', 'type', 'created_date', 'updated_date', 'is_deleted', 'project'
        )
        read_only_fields = ('id', 'created_date', 'updated_date', 'status', 'type', 'project')


class StatusSerializer(serializers.ModelSerializer):
    issue = IssueSerializer(many=True, read_only=True)

    class Meta:
        model = Status
        fields = ('id', 'name', 'issue')
        read_only_fields = ('id', 'issue')
