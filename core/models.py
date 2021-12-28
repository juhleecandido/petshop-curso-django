from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    animal = models.CharField(max_length=255)

    def __str__(self):
        return self.animal


class Distribuidora(models.Model):
    nome = models.CharField(max_length=255)
    site = models.URLField()

    def __str__(self):
        return self.nome


class Marca(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Racao(models.Model):
    mome = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    preco = models.FloatField()
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="racao")
    distribuidora = models.ForeignKey(
        Distribuidora, on_delete=models.PROTECT, related_name="racao")
    marcas = models.ManyToManyField(Marca, related_name="racao")


class Compra(models.Model):

    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, 'Carrinho'
        REALIZADO = 2, 'Realizado'
        PAGO = 3, 'Pago'
        ENTREGUE = 4, 'Entregue'

    usuario = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="compras")
    status = models.IntegerField(
        choices=StatusCompra.choices, default=StatusCompra.CARRINHO)


class ItensCompra(models.Model):
    compra = models.ForeignKey(
        Compra, on_delete=models.CASCADE, related_name="itens")
    racao = models.ForeignKey(
        Racao, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField()
