from django.db import models

# Create your models here.
class tbl_category(models.Model):
    category_name = models.CharField(max_length=100, null=True)
    category_image = models.ImageField(null=True,upload_to='media')

class tbl_subcategory(models.Model):
    category = models.ForeignKey(tbl_category, on_delete=models.CASCADE, null=True)
    subcategory_name = models.CharField(max_length=100, null=True)
    subcategory_image = models.ImageField(null=True,upload_to='media')




class tbl_Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    grams = models.CharField(max_length=100)
    pieces = models.CharField(max_length=100)
    serves = models.CharField(max_length=100)
    market_price= models.FloatField()
    our_price = models.FloatField()
    image = models.ImageField(null=True,upload_to='media')
    sub_category = models.ForeignKey(tbl_subcategory, on_delete=models.CASCADE)

class tbl_buy_now(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country =  models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    town_city = models.CharField(max_length=100)
    state_country = models.CharField(max_length=100)
    zip = models.IntegerField(null=True)
    phone =  models.IntegerField(null=True)
    email = models.EmailField(null=True)
    product =  models.ForeignKey(tbl_Products, on_delete=models.CASCADE , null=True)




class tbl_sign_up(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100, null=True)



class tbl_cart(models.Model):
    quantity = models.IntegerField(null=True)
    session_key = models.CharField(max_length=100)
    product = models.ForeignKey(tbl_Products, on_delete=models.CASCADE, null=True)

    def get_total(self):
        return self.quantity*self.product.our_price

class tbl_checkout(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    town_city = models.CharField(max_length=100)
    state_country = models.CharField(max_length=100)
    zip = models.IntegerField(null=True)
    phone =  models.IntegerField(null=True)
    email = models.EmailField(null=True)
    cart_total = models.FloatField()

class tbl_checkout_products(models.Model):
    quantity = models.IntegerField(null=True)
    product = models.ForeignKey(tbl_Products, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(tbl_sign_up, on_delete=models.CASCADE, null=True)
    checkout = models.ForeignKey(tbl_checkout, on_delete=models.CASCADE, null=True)

class tbl_contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    phone = models.IntegerField(null=True)
    message = models.CharField(max_length=100)

class tbl_add_blog(models.Model):
     blog_title = models.CharField(max_length=100)
     blog_content = models.CharField(max_length=100)




