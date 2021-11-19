from django.db import models

# Create your models here.
class Bacon(models.Model):
    name = models.CharField(max_length=80)
    gostosura = models.IntegerField()

# Depois q fizer iss aqui Î , de esse comando quenem você daria o runserver:   python manage.py makemigrations
# Ele vai criar um arquivo que vai gerar uma tabela dessa classe que foi escrita, senão dá erro.
# Mas gerar o arquivo não e suficiente, precisa rodar ele, então logo em seguida você usa esse:   python manage.py migrate