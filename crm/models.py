from django.db import models


class Customer(models.Model):    
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.phone} {self.active}"

    class Meta:
        verbose_name_plural = "Customers"

class Employee(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    rg = models.CharField(max_length=255, null=True, blank=True)
    cpf = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} {self.occupation} {self.rg} {self.cpf} {self.active}"

    class Meta:
        verbose_name_plural = "Employees"

