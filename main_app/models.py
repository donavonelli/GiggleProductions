from django.db import models

# Create your models here.
class Newsletter(models.Model):
    first_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f" User first name: {self.first_name} Email: {self.email}"