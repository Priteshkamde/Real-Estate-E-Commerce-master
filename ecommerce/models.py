from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class CustomUser(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    type = models.CharField(max_length=100, choices=(('seller', 'seller'), ('buyer', 'buyer'),))

    def __str__(self):
        return self.username


class Properties(models.Model):
    property_title = models.CharField(max_length=10000)
    buy_rent = models.CharField(max_length=10000, choices=(('Sale', 'Sale'), ('Rent', 'Rent')))
    locality = models.CharField(max_length=10000)
    property_type = models.CharField(max_length=10000, choices=(('Flat', 'Flat'), ('House/Villa', 'House/Villa'),
                                                                ('Plot', 'Plot'), ('Office Space', 'Office Space'),
                                                                ('Other Commercial', 'Other Commercial'),
                                                                ('Shop/Showroom', 'Shop/Showroom'), ('PG', 'PG')))
    price = models.IntegerField()
    BHK = models.CharField(max_length=10000,
                           choices=(('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('>5', '>5')))
    construction_status = models.CharField(max_length=100, choices=(
        ('Under Construction', 'Under Construction'), ('Ready To Move', 'Ready To Move')))
    area = models.IntegerField()
    address = models.CharField(max_length=10000)
    description = models.CharField(max_length=10000)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.property_title


class Comments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    property_title = models.CharField(max_length=10000)
    datetime = models.CharField(max_length=100)
    comment = models.CharField(max_length=50000)