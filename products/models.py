from django.db import models


class CategoryClass(models.Model):

    name = models.CharField(max_length=100, verbose_name='种类名称')

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class ProductClass(models.Model):

    name = models.CharField(max_length=128, verbose_name='产品名称')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='产品价格')
    count = models.IntegerField(default=0, verbose_name='产品库存')
    category = models.ForeignKey('CategoryClass', on_delete=models.CASCADE, verbose_name='产品种类', related_name='products_set')

    class Meta:

        db_table = 'products'


    # 根据外键将类目的名称呈现过来，相当于又新加一个字段
    # 应对第二种方法
    # @property
    # def category_name(self):
    #     return self.category.id, self.category.name

