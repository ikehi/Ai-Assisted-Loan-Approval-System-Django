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
    contact_no = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100,default='India')  # Added field for country
    no_of_dependents = models.IntegerField()
    education = models.IntegerField(choices=[(0, '0'), (1, '1')],default=1)
    employment_status = models.IntegerField(default=1)
    income_annum = models.DecimalField(max_digits=12, decimal_places=2 , default=0)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    loan_term = models.IntegerField(help_text="Loan term in years")
    cibil_score = models.IntegerField()
    residential_assets_value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    commercial_assets_value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    luxury_assets_value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    bank_asset_value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    application_date = models.DateTimeField(auto_now_add=True)
    passport_photo = models.ImageField(upload_to='passport_photos/', null=True, blank=True)
    ml_prediction = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.loan_amount}'