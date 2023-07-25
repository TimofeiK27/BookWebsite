from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=300)
    def serialize(self):
        return {
            "title": self.title,
            "description": self.description,
            "id": self.id,
        }
