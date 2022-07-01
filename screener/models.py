from django.db import models

# Create your models here.

class Company(models.Model):
    company_id = models.CharField(max_length=50, primary_key=True)
    company_name = models.CharField(max_length=100)
    company_code = models.CharField(max_length=100)
    company_group = models.CharField(max_length=100)
    company_industry = models.CharField(max_length=100)
    face_value = models.CharField(max_length=10)
    isin_number = models.CharField(max_length=100)

    
    class Meta:
        get_latest_by = 'company_id'


    def __str__(self):
        return self.company_name
    


