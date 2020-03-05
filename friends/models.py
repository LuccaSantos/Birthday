from django.db import models
from django.contrib.auth import get_user_model



class Friend(models.Model):
    name = models.CharField(max_length=250, default="")
    birthday = models.DateField()
    age = models.IntegerField()
    gift = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # test = models.IntegerField()

    # created_at = models.DateField(auto_now_add=True)
    # updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
