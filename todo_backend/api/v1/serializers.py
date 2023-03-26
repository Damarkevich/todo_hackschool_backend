from rest_framework import serializers
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False, read_only=True)
    assigned_to = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'pub_date',
            'image',
            'author',
            'assigned_to',
            'completed',
        )
