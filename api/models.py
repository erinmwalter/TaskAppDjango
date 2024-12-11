from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed')
    ]

    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = 'PENDING'
    )
    priority = models.CharField(
        max_length = 20,
        choices = PRIORITY_CHOICES,
        default = 'MEDIUM'
    )
    due_date = models.DateTimeField(null = True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title