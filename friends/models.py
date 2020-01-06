from django.db import models

class Friend(models.Model):
    name = models.CharField(max_length=250)
    birthday = models.CharField(max_length=15)
    age = models.IntegerField()
    gift = models.TextField()


    # created_at = models.DateField(auto_now_add=True)
    # updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
