from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from userApp.manager import *
import uuid

# Create your models here.

class Myuser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    full_name = models.CharField(max_length=200, verbose_name="Full Name")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    user = models.ForeignKey(Myuser, on_delete=models.CASCADE, related_name='address')
    address = models.CharField(max_length=300)
    landmark = models.CharField(max_length=255,null=True,blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.BigIntegerField()
    Mobile = models.BigIntegerField()