from django.db import models

# Create your models here.
class Messages(models.Model):
    MessageId=models.AutoField(primary_key=True)
    fromUser=models.CharField(max_length=500)
    toUser=models.CharField(max_length=500)

class Profiles(models.Model):
    profileId=models.AutoField(primary_key=True)
    emailId=models.CharField(max_length=500)
    firstName=models.CharField(max_length=500)
    lastName=models.CharField(max_length=500)
    profilePhotoUrl=models.CharField(max_length=500)
