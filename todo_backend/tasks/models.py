from django.db import models
from users.models import User
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(
        verbose_name='Title',
        max_length=100,
        blank=False,
        null=False,
        help_text='Enter title'
    )

    description = models.TextField(
        verbose_name='Description',
        help_text='Enter task description'
    )

    completed = models.BooleanField(default=False)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='users_tasks',
        verbose_name='Author',
        help_text='Enter task author'
    )

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='tasks_for_user',
        verbose_name='assigned_to',
        help_text='Appoint responsible'
    )

    pub_date = models.DateTimeField(
        verbose_name='Creation date',
        auto_now_add=True,
        db_index=True,
        help_text='Enter creation date',
    )

    due_date = models.DateTimeField(
        verbose_name='Due date',
        db_index=True,
        default=timezone.now()
        help_text='Enter due date',
    )

    image = models.ImageField(
        'Image',
        upload_to='media/tasks/',
        blank=True,
        null=True,
        help_text='upload image'
    )

    def _str_(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['-pub_date']
