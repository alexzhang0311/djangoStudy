from django.db import models

# Create your models here.

class OrmBook(models.Model):
    id = models.AutoField(primary_key=True) #可以不用写，django会自动创建自增主键
    name = models.CharField(max_length=100,null=False)
    author = models.CharField(max_length=100,null=False)
    price = models.FloatField(null=False,default=0)

    def __str__(self):
        return f"<Book:({self.name},{self.author},{self.price})>"