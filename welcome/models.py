from django.db import models

class Books(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images')

    def __str__(self):
        return f"{self.title}"