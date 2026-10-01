from django.db import models

class StudyTask(models.Model):
    """Store a study task entered by the user."""
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    minutes = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a readable name for a study task."""
        return f"{self.subject}: {self.title}"
