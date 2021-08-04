from django.db import models

# Create your models here.


class Blog(models.model):
    title = models.CharField(blnak=False, null=False, max_length=150)
    text = models.TextField(blank=True)
    created_detetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
