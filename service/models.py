from django.db import models


class Service(models.Model):    
    description = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=0.0)
    comission = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=0.0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.description} {self.price} {self.comission}"

    class Meta:
        verbose_name_plural = "Services"

class Order(models.Model):    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    payment_type = models.CharField(max_length=255, null=True, blank=True)
    paid = models.BooleanField()
    value = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=0.0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer} {self.payment_type} {self.paid} {self.value}"

    class Meta:
        verbose_name_plural = "Orders"

class OrderItems(models.Model):    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True, default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=0.0)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    comission_employee = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=0.0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.order} {self.service} {self.quantity} {self.price} {self.employee} {self.comission_employee}"

    class Meta:
        verbose_name_plural = "Orderitem"

