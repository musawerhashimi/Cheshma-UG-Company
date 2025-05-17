from django.db import models

    
class Category(models.Model):
    category_name= models.CharField(max_length=20)

    def __str__(self):
        return str(self.category_name)
    
class Product(models.Model):
    name= models.CharField(max_length=12)
    description= models.CharField(max_length=200)
    image= models.ImageField(upload_to="products/")
    category_name=models.ForeignKey(Category,related_name='cname',blank=False,null=False,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
    
class Partner(models.Model):
    name= models.CharField(max_length=30)
    image= models.ImageField(upload_to="partner/")

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name= 'Partner'
        verbose_name_plural= "Clients"
    
class News(models.Model):
    title= models.CharField(max_length=35)
    description= models.CharField(max_length=200)
    publish_date= models.DateField(auto_now_add=True)
    image= models.ImageField(upload_to="news/")

    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name= 'News'
        verbose_name_plural= "News"
    
class Contact(models.Model):
    name= models.CharField(max_length=20)
    lastname= models.CharField(max_length=20)
    gender= models.CharField(max_length=1,choices=[
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
    ])
    email= models.EmailField()
    subject= models.CharField(max_length=20)
    comment= models.CharField(max_length=70)
    send_date= models.DateField( auto_now_add=True)
    def __str__(self):
            return str(self.name)
    class Meta:
        verbose_name= 'Contact'
        verbose_name_plural= "Customers Message"

    

class Founder(models.Model):
    name= models.CharField(max_length=25)
    position= models.CharField(max_length=25)
    bio=models.CharField(max_length=70)
    image= models.ImageField(upload_to="founder/")

    def __str__(self):
        return str(self.name)
class Background(models.Model):
    image= models.ImageField(upload_to='bg/')