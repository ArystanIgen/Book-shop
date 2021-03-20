from django.db import models
from django.contrib.auth.models import User


TYPE_1=1
TYPE_2=2
TYPE_3=3
TYPE_4=4
TYPES = (
    (TYPE_1, 'Bullet'),
    (TYPE_2, 'Food'),
    (TYPE_3, 'Travel'),
    (TYPE_4, 'Sport'),
)



# Create your models here.
class BookJournalBase(models.Model):
    name=models.CharField(max_length=255, verbose_name="название")
    price=models.IntegerField(default=0, verbose_name='Стоимость')
    description=models.TextField(null=True, blank=True, verbose_name="Описание")
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="Добавлен")

    class Meta:
        abstract = True

class Book(BookJournalBase):
    num_pages=models.IntegerField(default=0, verbose_name='Количество страниц')
    genre=models.CharField(max_length=255, verbose_name="Жанр")

class Journal(BookJournalBase):
    type=models.SmallIntegerField(choices=TYPES, default=TYPE_1)
    publisher=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Владелец")