from django.db import models

# Create your models here.

property_type = (
    ('Sale', "sale"),
    ('Rent', "rent")
)

class Property(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField( max_length=80)
    type = models.CharField(choices=property_type, max_length=50)
    category = models.ForeignKey("Category",null=True , on_delete=models.SET_NULL)
    price = models.PositiveIntegerField()
    area = models.DecimalField( max_digits=5, decimal_places=2)
    rooms_number = models.PositiveIntegerField()
    beds_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property/', height_field=None, width_field=None, max_length=None)


    class Meta:
        verbose_name = ("Property")
        verbose_name_plural = ("properties")

    def __str__(self):
        return self.name





class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_image = models.ImageField(upload_to='category/', height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categories")

    def __str__(self):
        return self.category_name




class Reserve(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    notes = models.TextField()

    class Meta:
        verbose_name = ("Reserve")
        verbose_name_plural = ("Reservations")

    def __str__(self):
        return self.name
