from django.db import models
# from django.utils.html import mark_safe
from django.contrib.auth.models import User

# Create your models here.
# class customer(models.Model):
#      name=models.CharField(max_length=250)
#      address=models.TextField()
#      email=models.EmailField()
#      phoneno=models.IntegerField()
#      psw=models.CharField(max_length=150)
#      repsw=models.CharField(max_length=150)

class Category(models.Model):
     title=models.CharField(max_length=50,verbose_name="category title")
     slug=models.SlugField(max_length=55,verbose_name="category slug")
     description=models.TextField(blank=True,verbose_name="category description")
     category_image=models.ImageField(upload_to="category",blank=True,null=True,verbose_name="category image")
     is_active=models.BooleanField(verbose_name="Is Active")
     is_featured=models.BooleanField(verbose_name="Is Featured")
     class Meta:
          verbose_name_plural='categories'
          

     def __str__(self):
        return self.title
     
class Product(models.Model):
      title=models.CharField(max_length=150,verbose_name="product title")
      slug=models.SlugField(max_length=150,verbose_name="product slug")
      sku=models.CharField(max_length=255,unique="True",verbose_name="unique product ID (SKU)")
      short_description=models.TextField(verbose_name="short description")
      detail_description=models.TextField(blank="True",null="True", verbose_name='detail description')
      product_image=models.ImageField(upload_to="product",blank="True",null="True",verbose_name="product image")
      price=models.DecimalField(max_digits=8,decimal_places=2)
      category=models.ForeignKey(Category, verbose_name="product categoy",on_delete=models.CASCADE)
      is_active=models.BooleanField(verbose_name="is active")
      is_featured=models.BooleanField(verbose_name="is featured")
      productStock=models.PositiveIntegerField()
      created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
      updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")
      class Meta:
          verbose_name_plural = 'Products'
          ordering = ('-created_at', )

      def __str__(self):
        return self.title
     

     #  def image_tag(self):
     #      return mark_safe('<img src="%s" width="50" height="50" />' % (self.product_image.url))
class Relatedimage(models.Model):
      products=models.ForeignKey(Product,default=None, on_delete=models.CASCADE)
      image=models.FileField(upload_to='relimg',null=True)  
class Contact(models.Model):
      email=models.EmailField()
      message=models.TextField()
class Cart(models.Model):
     user=models.ForeignKey(User,verbose_name='User',on_delete=models.CASCADE)
     product=models.ForeignKey(Product,verbose_name='Product',on_delete=models.CASCADE)
     quantity=models.PositiveIntegerField(default='1',verbose_name='quantity')
       
     def __str__(self):
          return str(self.user)
     @property
     def total_price(self):
          return self.quantity*self.product.price
