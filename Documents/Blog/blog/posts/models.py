from django.db import models
from django.contrib.auth.models import User
#from datetime import datetime

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile.pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100000)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    #created_at = models.DateTimeField(null=True, default=datetime.now, blank=True)
    #test = models.CharField(default ='', max_length=100)

