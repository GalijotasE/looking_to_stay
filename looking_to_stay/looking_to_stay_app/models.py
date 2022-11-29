from django.db import models


class Category(models.Model):
    id = models.AutoField('Unique ID', primary_key=True)
    category_name = models.CharField('Category', max_length=128, help_text='Please type a name of the category')

    def __str__(self) -> str:
        return self.category_name

    class Meta:
        ordering = ['category_name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

