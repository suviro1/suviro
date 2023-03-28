from django.db import models
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
# Create your models here.

USECASE_CHOICES = {
('food', 'Food'),
('pharmaceutical_Bio','Pharmaceutical_Bio'),
('precision_machine','Precision_machine'),
('electronics_industry','Electronics_industry'),
('facility_management','Facility_management'),
('water_treatment','Water_treatment'),
('smart_Farm','Smart_Farm'),
('oem','Oem'),
}
class Usecases(models.Model):
    category = models.CharField(choices=USECASE_CHOICES,max_length=50)
    title = models.CharField(max_length=200)
    image = CloudinaryField('image')
    description = models.TextField()
    def __str__(self):
        return str(self.title)


class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.product_type} - {self.company.name}"








class Product(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField(max_length=500)
    
    description = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    
    tags = models.CharField(max_length=50)
    product_img1 = CloudinaryField('image')
    product_img2 = CloudinaryField('image')
    product_img3 = CloudinaryField('image')
    product_img4 = CloudinaryField('image')
    moredetails = HTMLField()

    def __str__(self):
        return str(self.title)

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone = models.BigIntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
