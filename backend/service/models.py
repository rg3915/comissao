from django.db import models
from django.urls import reverse_lazy

from backend.crm.models import Customer, Employee


class Service(models.Model):
    description = models.CharField('descrição', max_length=255, unique=True)
    price = models.DecimalField(
        'preço',
        max_digits=5,
        decimal_places=2,
        default=0.0
    )
    comission = models.DecimalField(
        'comissão',
        max_digits=5,
        decimal_places=2,
        default=0.0
    )
    created = models.DateTimeField('criado em', auto_now_add=True)
    updated = models.DateTimeField('modificado em', auto_now=True)

    class Meta:
        ordering = ('description',)
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return f'{self.description}'

    def get_absolute_url(self):
        return reverse_lazy('service:service_detail', kwargs={'pk': self.pk})


PAYMENT_TYPE = (
    ('di', 'Dinheiro'),
    ('de', 'Débito'),
    ('cr', 'Crédito'),
    ('pix', 'Pix'),
    ('dep', 'Depósito'),
)


class Order(models.Model):
    customer = models.ForeignKey(
        Customer,
        verbose_name='cliente',
        on_delete=models.CASCADE,
        null=True
    )
    payment_type = models.CharField(
        'tipo de pagamento',
        max_length=3,
        choices=PAYMENT_TYPE,
        default='di'
    )
    paid = models.BooleanField('pago?', default=False)
    value = models.DecimalField(
        'valor',
        max_digits=5,
        decimal_places=2,
        null=True,
        default=0.0
    )
    created = models.DateTimeField('criado em', auto_now_add=True)
    updated = models.DateTimeField('modificado em', auto_now=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f'{str(self.pk).zfill(3)}'

    def get_absolute_url(self):
        return reverse_lazy('service:order_detail', kwargs={'pk': self.pk})


class OrderItems(models.Model):
    order = models.ForeignKey(
        Order,
        verbose_name='ordem',
        on_delete=models.CASCADE,
        null=True
    )
    service = models.ForeignKey(
        Service,
        verbose_name='serviço',
        on_delete=models.CASCADE,
        null=True
    )
    quantity = models.IntegerField('quantidade', default=1)
    price = models.DecimalField(
        'preço',
        max_digits=5,
        decimal_places=2,
        null=True,
        default=0.0
    )
    employee = models.ForeignKey(
        Employee,
        verbose_name='funcionário',
        on_delete=models.CASCADE,
        null=True
    )
    comission_employee = models.DecimalField(
        'comissão',
        max_digits=5,
        decimal_places=2,
        null=True,
        default=0.0
    )
    created = models.DateTimeField('criado em', auto_now_add=True)
    updated = models.DateTimeField('modificado em', auto_now=True)

    class Meta:
        ordering = ('order', 'pk')
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens do Pedido'

    def __str__(self):
        return f'{self.order} {str(self.pk).zfill(3)}'
