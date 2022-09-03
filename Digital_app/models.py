from django.db import models

# Create your models here.

class Registered_user(models.Model):
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=10)


    class Meta:
        db_table ='RegisteredUser'

    def __str__(self) -> str:
        return self.email

    
    
class User_data(models.Model):
    Registered_user = models.ForeignKey(Registered_user,on_delete=models.CASCADE)
    name = models.CharField(max_length=25, default='', blank=True, null=True)
    profile_image = models.FileField(upload_to='images/',default='images/user.png')
    address = models.CharField(max_length=25, default='', blank=True, null=True)
    country = models.CharField(max_length=25, default='', blank=True, null=True)
    dob = models.DateField( blank=True, null=True)
    phone = models.CharField(max_length=10, default='', blank=True, null=True)
    gender = models.CharField(max_length=10, default='', blank=True, null=True)
    member = models.CharField(max_length=10, default='', blank=True, null=True)
    alternate_contact_no = models.CharField(max_length=10, default='', blank=True, null=True)
    vehicle_no = models.CharField(max_length=20, default='', blank=True, null=True)
    total_vehicle = models.CharField(max_length=10, default='', blank=True, null=True) 


    class Meta:
        db_table ='UserData'

    def __str__(self) -> str:
        return self.Registered_user.email