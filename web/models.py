from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, full_names, phone_number, location, password=None, **extra_fields):
        if not full_names:
            raise ValueError('The Full Names field is required.')
        if not phone_number:
            raise ValueError('The Phone Number field is required.')
        if not location:
            raise ValueError('The Location field is required.')
        user = self.model(
            full_names=full_names,
            phone_number=phone_number,
            location=location,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,full_names, phone_number, location,password=None):
        user = self.create_user(
            full_names = full_names,
            location = location,
            phone_number = phone_number,
            password = password
            
        )

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
class CustomUser(AbstractBaseUser):
    full_names = models.CharField(max_length=255, blank=False, null=False)
    phone_number = models.CharField(max_length=15, unique=True, blank=False, null=False)
    location = models.CharField(max_length=255, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_names', 'location']

    objects = UserManager()

    def __str__(self):
        return self.full_names

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
class Categorie(models.Model):
    cat_choices = (
        ("Fruits","Fruits"),("Foods","Foods"), ("Drinks","Drinks")
    )
    
    name = models.CharField(max_length=500,null=True,choices=cat_choices,default="Foods")
    
    def __str__(self):
        return self.name

class DrinksCategorie(models.Model):
    cat = (
        ("Soft Drinks","Soft Drinks"),
        ("Drink","Drink"),
        ("Cocktail","Cocktail")
    )
    
    drink_name = models.CharField(max_length=200,choices=cat)
    
    def __str__(self):
        return self.drink_name

    
class FruitssCategorie(models.Model):
    cat = (
        ("Fruits","Fruits"),
        ("Juices","Juices"),
        ("Fruit Salad","Fruit Salad"),
    )
    
    category_name = models.CharField(max_length=200,choices=cat,default="Fruits")
    
    def __str__(self):
        return self.category_name
    
class PricessCategorie(models.Model):
    cat = (
        ("Normal","Normal"),
        ("Advanced","Advanced"),
        ("VIP","VIP"),
    )
    
    p_name = models.CharField(max_length=200,choices=cat,default="Normal")
    
    def __str__(self):
        return self.p_name
    

    
    
class Food(models.Model):
    name = models.CharField( max_length=400)
    image = models.CharField(max_length=700)
    description = models.TextField()
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Fruits(models.Model):
    name = models.CharField( max_length=400)
    image = models.CharField(max_length=700)
    description = models.TextField()
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    in_category = models.ForeignKey(FruitssCategorie,on_delete=models.CASCADE,null=True)
    price_category = models.ForeignKey(PricessCategorie,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name
    
    
class Drink(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=500)
    description = models.TextField()
    price= models.IntegerField()
    category = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    drink_category = models.ForeignKey(DrinksCategorie,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class CockTail(models.Model):
    cocktail_name = models.CharField(max_length=200)
    cocktail_image = models.CharField(max_length=500)
    cocktail_description = models.TextField()
    cocktail_price= models.IntegerField()
    cocktail_category = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.cocktail_name
    
class Order(models.Model):
    item_id = models.IntegerField()
    category= models.IntegerField()
    order_count = models.IntegerField()
    order_price = models.IntegerField()
    order_made_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    order_added_on = models.DateTimeField(auto_now_add=True)

    
    
    
    def __str__(self):
        return self.item_id
    
class OrderCheckout(models.Model):
    item = models.IntegerField()
    category = models.IntegerField()
    order_amount = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    order_made_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    order_price = models.IntegerField()
    
class Checkout(models.Model):
    orderer =  orderer=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    ordered_items = models.CharField(max_length=1000)
    order_total_price = models.IntegerField()
    order_placed_at = models.DateTimeField(auto_now_add=True)
    latitude = models.CharField(max_length=700,null=True)
    longitude = models.CharField(max_length=200,null=True)
    order_status = (("Delivered","Delivered"),
                    ("Pending","Pending")
                    )
    order_status = models.CharField(max_length=200,choices=order_status, default=order_status[1][0],null=True)
    order_number = models.CharField(max_length=100)
    
class whishlist(models.Model):
    category= models.IntegerField()
    item_id= models.IntegerField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.item_id
    
class Banners(models.Model):
    banner = models.CharField(max_length=1000)
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    
    