from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    Personel = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})

class Business(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    Personel = models.ForeignKey(User, on_delete=models.CASCADE) 
    image = models.ImageField(  upload_to="profile_pics")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('business_detail', kwargs={'pk':self.pk})

def __str__(self):
        return " %s Profile" % self.user
    

def save(self):
    super().save()  #save method of the parent class

    img = Image.open(self.image.path) 

    if img.height > 700 or img.width > 700:
        output_size = (500,500) #maximum picture size
        img.thumbnail(output_size) #resizing our image
        img.save(self.image.path)