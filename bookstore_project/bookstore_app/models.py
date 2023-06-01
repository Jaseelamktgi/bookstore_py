from django.db import models
# Create your models here.
class Books(models.Model):
    image = models.ImageField(upload_to='books')
    book_name = models.CharField(max_length=300, )
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.book_name
