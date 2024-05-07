from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Books(models.Model):
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='books/', blank=True, null=True)
    year = models.IntegerField()
    book_category = models.CharField(max_length=100)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.book_name