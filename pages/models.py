from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
# Create your models here.
class Book(models.Model):
    status_book=[
        ('solid','solid'),
        ('rental','rental'),
        ('avirable','avirable'),
        ]
    title=models.CharField(max_length=100,verbose_name=_('name_book'))
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='book_author')
    photo_book=models.ImageField(upload_to='phot_book/%y-%m-%d',null=True,blank=True)
    photo_author=models.ImageField(upload_to='photo_author/%y-%m-%d',null=True,blank=True)
    pages=models.IntegerField(null=True,blank=True)
    price=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    price_rental=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    period_rental=models.IntegerField(null=True,blank=True)
    active=models.BooleanField(default=True)
    status=models.CharField(max_length=25,choices=status_book)
    category=models.ForeignKey('Category',on_delete=models.CASCADE,related_name='book_category')
    slug=models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Book,self).save(*args,**kwargs)
    
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name



