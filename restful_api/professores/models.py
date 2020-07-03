from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    nascimento = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
