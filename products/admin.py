from django.contrib import admin
from products.models import Products, Variations, ReviewRating, ProductGallery

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display= ('product_name','price','stock','category','modified_date','is_available')
    prepopulated_fields = {'slug': ('product_name',)}

class VariationAdmin(admin.ModelAdmin):
    list_display= ('product','variation_category','variation_value','is_active')
    list_editable= ('is_active',)
    list_filter = ('product','variation_category','variation_value')

admin.site.register(Products, ProductAdmin)
admin.site.register(Variations, VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)