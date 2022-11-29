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

class Hotel(models.Model):
    id = models.AutoField('Unique ID', primary_key=True)
    hotel_name = models.CharField('Hotel Name', max_length=100, help_text="Please enter a name of the Hotel")
    description = models.TextField('Description', max_length=10000,
        help_text='Please enter a description of the hotel, consisting up to 10000 words.')
    company_id = models.ForeignKey(
        Company, on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    city_id = models.ForeignKey(
        City, on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    category_id = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    cover_photo = models.ImageField('Cover Photo', upload_to='covers', blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.hotel_name}"

    class Meta:
        ordering = ['hotel_name', 'company_id']
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'