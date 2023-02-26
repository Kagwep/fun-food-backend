from django.contrib import admin

from .models import Order,whishlist,Categorie,CockTail,Food,Drink,DrinksCategorie,Fruits,FruitssCategorie


class DrinkAdmin(admin.ModelAdmin):
    list_display = ('__all__',)
    list_filter = ('drink_category',)
    
    search_fields = ('name',)
    ordering = ('name','price')
    filter_horizontal = ()
    

admin.site.register(Drink, DrinkAdmin)

class FruitAdmin(admin.ModelAdmin):
    list_display = ('__all__',)
    list_filter = ('in_category',)
    
    search_fields = ('name',)
    ordering = ('name','price')
    filter_horizontal = ()
    

admin.site.register(Fruits, FruitAdmin)



admin.site.register(Order)
admin.site.register(whishlist)
admin.site.register(Categorie)
admin.site.register(CockTail)
admin.site.register(Food)

admin.site.register(DrinksCategorie)
admin.site.register(FruitssCategorie)
