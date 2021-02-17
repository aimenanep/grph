from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=255,blank=True)
    description=models.TextField(blank=True,null=True)
    category=models.ForeignKey("categories.Category",on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.title
