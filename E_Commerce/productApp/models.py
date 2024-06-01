from django.db import models
from userApp.models import Myuser as User
import uuid

# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100,unique=True)

    def __str__(self) -> str:
        return self.name

class subCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE,default="0d5b4d40-dd0c-477a-ae3b-873ba9ae7331")
    name = models.CharField(max_length=100,unique=True)

    def __str__(self) -> str:
        return self.name

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100,unique=True)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subCategory = models.ForeignKey(subCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self) -> str:
        return self.name

class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.email

class CartItem(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    Totalprice = models.FloatField(default=0.0)

    def save(self,*args,**kwargs):
        print(self.Totalprice)
        self.Totalprice = self.product.price * self.quantity
        super().save(*args,**kwargs)

class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.FloatField(default=0)
    review = models.TextField(null=True,blank=True)
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Rating = {self.rating}\nReview = {self.review}'