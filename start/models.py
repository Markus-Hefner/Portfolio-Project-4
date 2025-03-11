from django.db import models

# Create your models here.

class Orchestra(models.Model):
    """
    Stores an orchestra entry related to :model:`auth.User`.
    """
    name = models.CharField(max_length=200, unique=True)
    organisation = models.CharField(max_length=200)
    conductor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orchestras"
    )
    info = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} | {self.organisation} | {self.info}| {self.created_on}"