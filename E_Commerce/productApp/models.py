from django.db import models
import uuid

# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100,unique=True)

    def __str__(self) -> str:
        return self.name

class subCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Category_id = models.ForeignKey(Category,on_delete=models.CASCADE,default="0d5b4d40-dd0c-477a-ae3b-873ba9ae7331")
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