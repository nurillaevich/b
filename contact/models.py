from django.db import models



class ContactUs(models.Model):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=212)