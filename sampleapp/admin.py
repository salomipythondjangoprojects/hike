from django.contrib import admin
from .models import Category,Product,Relatedimage,Contact
# Register your models here.
# class customerAdmin(admin.ModelAdmin):
#     list_display=('name','address','email','phoneno')
#     exclude=('psw','repsw')
class categoryAdmin(admin.ModelAdmin):
    list_display=('title','slug','category_image','is_featured','is_active')
    list_editable=('slug','is_active','is_featured')
    list_filter=('is_active','is_featured')
    search_fields=('title','description')
    prepopulated_fields={"slug":("title",)}

class RelatedimageAdmin(admin.StackedInline):
      model=Relatedimage

class ProductAdmin(admin.ModelAdmin):
      list_display=('title','slug','product_image','is_active','is_featured','price','short_description')
      list_editable=('slug','is_active','is_featured')
      list_filter=('is_active','is_featured')
      search_fields=('title','short_description','price','detail_description')
      prepopulated_fields={"slug":("title",)}
      inlines=[RelatedimageAdmin]

      

# 
# admin.site.register(customer,customerAdmin)
admin.site.register(Category,categoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Contact)