from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)

class ProductImageAdmin(admin.StackedInline):
    model =ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title' , 'price' ]
    inlines = [ProductImageAdmin]
admin.site.register(Product ,ProductAdmin)


@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ['color' , 'price']
    model = ColorVariant

@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['size' , 'price']
    model = SizeVariant

