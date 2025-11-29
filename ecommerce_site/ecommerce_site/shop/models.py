# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.
# from django.db import models
# from django.db import models


# class AboutVideo(models.Model):
#     title = models.CharField(max_length=200)
#     video_file = models.FileField(upload_to="about_videos/")
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title


# class Image(models.Model):
#     image = models.ImageField(upload_to='images/')
#     caption = models.CharField(max_length=255)
#     caption1 = models.CharField(max_length=255)


# def __str__(self):
#         return self.caption1
      
# def __str__(self):
#         return self.caption
   
   
# class Pics(models.Model):
#     image = models.ImageField(upload_to='images/')
#     caption = models.CharField(max_length=255)
#     caption1 = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.caption
 
        
        
        
        
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='products/')
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return self.name


# class ContactMessage(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

        
        
    
#     class Iphone(models.Model):
#         image = models.ImageField(upload_to='images/')
#         Caption = models.CharField(max_length=255)
#         Caption1 = models.CharField(max_length=255)
        
#         def __str__(self):
#             return self.Caption

from django.db import models

class AboutVideo(models.Model):
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to="about_videos/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=255)
    caption1 = models.CharField(max_length=255)

    def __str__(self):
        return self.caption


class Pics(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=255)
    caption1 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.caption


class Iphone(models.Model): 
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=255)
    caption1 = models.CharField(max_length=255)

    def __str__(self):
        return self.caption


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
