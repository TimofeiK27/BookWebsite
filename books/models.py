from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=300)
    requests = models.CharField(max_length=25, default=0)
    def serialize(self):
        return {
            "title": self.title,
            "description": self.description,
            "requests": self.requests,
            "id": self.id,
        }
    
class Request(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    email = models.CharField(max_length=30)
