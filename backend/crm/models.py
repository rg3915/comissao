from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy


class Customer(models.Model):
    first_name = models.CharField('nome', max_length=255)
    last_name = models.CharField('sobrenome', max_length=255, null=True, blank=True)  # noqa E501
    email = models.EmailField('e-mail', max_length=254, null=True, blank=True)
    phone = models.CharField('telefone', max_length=255, null=True, blank=True)
    active = models.BooleanField('ativo', default=True)
    created = models.DateTimeField('criado em', auto_now_add=True)
    updated = models.DateTimeField('modificado em', auto_now=True)

    class Meta:
        ordering = ('first_name',)
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name or ""}'.strip()

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse_lazy('crm:customer_detail', kwargs={'pk': self.pk})


class Employee(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='usuário',
        on_delete=models.CASCADE,
        null=True
    )
    occupation = models.CharField('cargo', max_length=50, null=True, blank=True)  # noqa E501
    rg = models.CharField('RG', max_length=9, null=True, blank=True)
    cpf = models.CharField('CPF', max_length=11, null=True, blank=True)
    active = models.BooleanField('ativo', default=True)
    created = models.DateTimeField('criado em', auto_now_add=True)
    updated = models.DateTimeField('modificado em', auto_now=True)

    class Meta:
        ordering = ('user__first_name',)
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return f'{self.user.get_full_name()}'

    def get_absolute_url(self):
        return reverse_lazy('crm:employee_detail', kwargs={'pk': self.pk})
