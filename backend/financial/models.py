from django.contrib.auth.models import User
from django.db import models

from backend.crm.models import Employee
from backend.service.models import OrderItems


class ComissionNote(models.Model):
    created_by = models.ForeignKey(User, verbose_name='criado por', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, verbose_name='funcionário', on_delete=models.CASCADE)
    payment_date = models.DateField('data de pagamento')
    paid = models.BooleanField('pago?', default=False)
    active = models.BooleanField('ativo', default=True)
    created = models.DateTimeField('criado em', auto_now_add=True)
    updated = models.DateTimeField('modificado em', auto_now=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'Nota de Comissão'
        verbose_name_plural = 'Notas de Comissão'

    def __str__(self):
        return f'{str(self.pk).zfill(3)}'


class ComissionNoteItems(models.Model):
    comission_note = models.ForeignKey(
        ComissionNote,
        verbose_name='nota de comissão',
        on_delete=models.CASCADE,
        null=True
    )
    order_items = models.ForeignKey(
        OrderItems,
        verbose_name='itens do pedido',
        on_delete=models.CASCADE,
        null=True
    )
    quantity = models.IntegerField('quantidade', null=True, default=1)
    comission = models.DecimalField('valor da comissão', max_digits=5, decimal_places=2, default=0.0)
    created = models.DateTimeField('criado em', auto_now_add=True)
    updated = models.DateTimeField('modificado em', auto_now=True)

    class Meta:
        ordering = ('comission_note', 'pk')
        verbose_name = 'Item da Nota de Comissão'
        verbose_name_plural = 'Itens da Nota de Comissão'

    def __str__(self):
        return f'{self.comission_note} {str(self.pk).zfill(3)}'
