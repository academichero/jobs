from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Job(models.Model):
    '''
        Modelo que representa as vagas cadastradas
    '''
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary_min = models.DecimalField(max_digits=10, decimal_places=2)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2)
    workload = models.PositiveIntegerField(validators =[MinValueValidator(0), MaxValueValidator(45)])
    validity = models.DateTimeField()
    open_job = models.BooleanField(default=True)
    internal_job = models.BooleanField(default=False)
    author = models.ForeignKey(User)
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'

    def __str__(self):
        return self.title
