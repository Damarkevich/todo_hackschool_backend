from rest_framework import serializers
from tasks.models import Task
from users.models import User


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )
    assigned_to = serializers.SlugRelatedField(
        queryset=User.objects.all(),
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
