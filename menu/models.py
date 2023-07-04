from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class bookReviews_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    review = models.TextField()
    isPublic =models.BooleanField(default=True)

    class Meta:
        verbose_name = "bookReviews"
        verbose_name_plural = "bookReviews"
    
    def __str__(self):
        return self.title
    
class todo_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = "todo"
        verbose_name_plural = "todo"

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,blank=True,null=True)
    last_name = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    bio = models.TextField(blank=True,null=True)
    Interest=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return str(self.user)