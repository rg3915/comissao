from django.db import models


class ComissionNote(models.Model):    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    payment_date = models.DateField()
    paid = models.BooleanField()
    active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.created_by} {self.employee} {self.payment_date} {self.paid} {self.active}"

    class Meta:
        verbose_name_plural = "Comissionnotes"

class ComissionNoteItems(models.Model):    
    comission_note = models.ForeignKey(ComissionNote, on_delete=models.CASCADE, null=True)
    order_items = models.ForeignKey(OrderItems, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True, default=0)
    comission = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=0.0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.comission_note} {self.order_items} {self.quantity} {self.comission}"

    class Meta:
        verbose_name_plural = "Comissionnoteitem"

