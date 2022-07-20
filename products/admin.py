from django.contrib import admin
<<<<<<< HEAD
from products.models import Products, Variations
=======
from products.models import Products
>>>>>>> aa6b27f (First Commit)

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display= ('product_name','price','stock','category','modified_date','is_available')
    prepopulated_fields = {'slug': ('product_name',)}

<<<<<<< HEAD
class VariationAdmin(admin.ModelAdmin):
    list_display= ('product','variation_category','variation_value','is_active')
    list_editable= ('is_active',)
    list_filter = ('product','variation_category','variation_value')

admin.site.register(Products, ProductAdmin)
admin.site.register(Variations, VariationAdmin)
=======
admin.site.register(Products, ProductAdmin)
>>>>>>> aa6b27f (First Commit)
