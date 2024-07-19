from django.db import models

# Create your models here.

from django.contrib.auth.models import User



class Application(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('R', 'Rejected'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact_no = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    cibil_score = models.IntegerField()
    income = models.DecimalField(max_digits=10, decimal_places=2)
    employment_status = models.CharField(max_length=50)
    loan_term = models.IntegerField(help_text="Loan term in years")
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    residential_assets = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    commercial_assets = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    application_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.loan_amount}'