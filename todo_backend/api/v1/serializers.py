from rest_framework import serializers
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False,
        slug_field='username'
    )
    assigned_to = serializers.SlugRelatedField(
        many=False,
        slug_field='username'
    )

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
