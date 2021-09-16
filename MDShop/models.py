from django.db import models 
from django.urls import reverse
from autoslug import AutoSlugField
from django.db.models.signals import pre_save
from datetime import date
from mptt.fields import  TreeForeignKey
from mptt.models import MPTTModel
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver


class Genre(models.Model):
    """Категория"""
    name        = models.CharField("Название категории", max_length=100)
    url         = models.SlugField(max_length=160, unique=True,verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class smartphone(models.Model):
    """Смартфоны"""
    def __str__(self):
        return self.title
    img1            =    models.ImageField(verbose_name='1.Изображения для слайдера',upload_to='photos',null=True, blank=True)
    img2            =    models.ImageField(verbose_name='2.Изображения для слайдера',upload_to='photos',null=True, blank=True)
    img3            =    models.ImageField(verbose_name='3.Изображения для слайдера',upload_to='photos',null=True, blank=True)
    img4            =    models.ImageField(verbose_name='4.Изображения для слайдера',upload_to='photos',null=True, blank=True)
    img5            =    models.ImageField(verbose_name='5.Изображения для слайдера',upload_to='photos',null=True, blank=True)
    img6            =    models.ImageField(verbose_name='6.Изображения для слайдера',upload_to='photos',null=True, blank=True)
    title           =    models.CharField(verbose_name='Заголовок',max_length=255)
    price           =    models.PositiveSmallIntegerField(verbose_name='Цена', default=2019)
    genres          =    models.ManyToManyField(Genre, verbose_name="Категории")
    slug            =    AutoSlugField(verbose_name='URL',populate_from='title' )
    pred1           =    models.CharField(max_length=255,verbose_name='Диагональ дисплея, дюйм',blank=True)
    pred2           =    models.CharField(max_length=255,verbose_name='Разрешение дисплея',blank=True)
    pred3           =    models.CharField(max_length=255,verbose_name='Операционная система',blank=True)
    pred4           =    models.CharField(max_length=255,verbose_name='Объем оперативной памяти',blank=True)
    pred5           =    models.CharField(max_length=255,verbose_name='Объём встроенной памяти',blank=True)
    pred6           =    models.CharField(max_length=255,verbose_name='Количество SIM-карт',blank=True)
    pred7           =    models.CharField(max_length=255,verbose_name='Стандарт связи',blank=True)
    pred8           =    models.CharField(max_length=255,verbose_name='Стандарт защиты от пыли и влаги',blank=True)

    class Meta:
            ordering=['-id']
            verbose_name = "Смартфон"
            verbose_name_plural = "Смартфоны" 


class Customer(models.Model):
    """Пользователи"""
    user            =    models.ForeignKey(User,on_delete=models.CASCADE,null=True,verbose_name='Пользователь')
    phone           =    models.CharField(max_length=11,blank=True,null=True,verbose_name='Номер телефона')
    first_name      =    models.CharField(max_length=30,null=True,blank=True,verbose_name='Имя')
    last_name       =    models.CharField(max_length=30,null=True,blank=True,verbose_name='Фамилия')
    email           =    models.EmailField(max_length=255,null=True,blank=True,verbose_name='Эл. адрес')
    
    class Meta:
            ordering=['-id']
            verbose_name = "Пользователь"
            verbose_name_plural = "Пользователи" 

    def __str__(self):
        return "User: {}, phone: {}".format(self.user, self.phone)

    @receiver(post_save, sender=get_user_model())
    def create_likeCustomer(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)
 

class CustomerLike(models.Model):
    """Избранное"""
    likeNEW         =    models.ForeignKey(smartphone,  on_delete=models.CASCADE, null=True,blank=True,verbose_name='Товар')
    likeCustomer    =    models.ForeignKey(Customer,    on_delete=models.CASCADE, null=True           ,verbose_name='Покупатель')
    created_at      =    models.DateTimeField(auto_now_add=True,null=True,blank=True,verbose_name='Время создания')
    updated_at      =    models.DateTimeField(auto_now=True,null=True,blank=True,verbose_name='Время изменения')

    class Meta:
            ordering=['-id']
            verbose_name = "Избранное"
            verbose_name_plural = "Избранное"

    @receiver(post_save, sender=Customer)
    def create_likeCustomer(sender, instance, created, **kwargs):
        if created:
            CustomerLike.objects.create(likeCustomer=instance)  

    def __str__(self):
        return self.created_at 


class CustomerAddress(models.Model):
    """Адрес доставка"""
    country          =    models.CharField(max_length=30,blank=True,verbose_name='Cтрана')
    town             =    models.CharField(max_length=30,blank=True,verbose_name='Город')   
    address          =    models.CharField(max_length=30,blank=True,verbose_name='Адрес')     
    house            =    models.CharField(max_length=30,blank=True,verbose_name='Дом')  
    apartment        =    models.CharField(max_length=30,blank=True,verbose_name='Квартира')  
    index            =    models.CharField(max_length=30,blank=True,verbose_name='Почтовый индекс')  
    addressCustomer  =    models.ForeignKey(Customer, on_delete=models.CASCADE,null=True,verbose_name='Покупателя')
    
    def __str__(self):
        return self.addressCustomer.phone   
    
    class Meta:
            ordering =      ['-id']
            verbose_name = "Адрес доставка"
            verbose_name_plural = "Адрес доставки"

class order(models.Model):
    """Заказы"""
    orderCustomer    =      models.ForeignKey(Customer, on_delete=models.CASCADE,null=True,verbose_name='Покупателя')
    smartphone       =      models.ManyToManyField(smartphone,verbose_name='Смартфон')
    orderAddress     =      models.ForeignKey(CustomerAddress, on_delete=models.CASCADE,null=True,verbose_name='Адрес покупателя')
    price            =      models.PositiveSmallIntegerField(blank=True,null=True,verbose_name='Цена')
  
    def __str__(self):
        return "{}.{}".format(self.orderCustomer.first_name , self.orderAddress )

    class Meta:
            ordering =      ['-id'] 
            verbose_name = "Заказ"
            verbose_name_plural = "Заказы"
