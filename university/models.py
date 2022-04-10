from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class Registration(models.Model):
    MARITAL_STATUS = (
        ('single','single'),
        ('married','married')
    )

    GENDER = (
        ('male','male'),
        ('female','female')
    )

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS)
    gender = models.CharField(max_length=10, choices=GENDER)
    height = models.FloatField()
    gsp_location = CountryField(blank_label='select country')
    cam_photo = models.ImageField(upload_to='images')
    iq_test = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     if self.age < 1 and self.height < 1:
    #         raise ValueError('Value cannot be -ve')
    #     super(Registration, self).save(*args, **kwargs)

    # class Meta:
    #     ordering = ["iq_test"]

