from django.db import models

# Create your models here.
class Empcomp(models.Model):
    employee_identifier = models.IntegerField(db_column='Employee Identifier', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    salaries = models.FloatField(db_column='Salaries', blank=True, null=True)  # Field name made lowercase.
    other_salaries = models.FloatField(db_column='Other Salaries', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_salary = models.FloatField(db_column='Total Salary', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    retirement = models.FloatField(db_column='Retirement', blank=True, null=True)  # Field name made lowercase.
    health_and_dental = models.FloatField(db_column='Health and Dental', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    other_benefits = models.FloatField(db_column='Other Benefits', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_benefits = models.FloatField(db_column='Total Benefits', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_compensation = models.FloatField(db_column='Total Compensation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'employee-compensation'