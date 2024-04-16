from django.db import models

class Footer(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()


    whatsapp = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)


class Message(models.Model):
    first_name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    body = models.TextField()




    def __str__(self):
        return f"{self.first_name}-----{self.email}"