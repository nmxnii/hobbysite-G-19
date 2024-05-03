from django.db import models
from django.urls import reverse


class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    people_required = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=(('open', 'OPEN'), ('full', 'FULL'),
                                       ('completed', 'COMPLETED'), ('discontinued', 'DISCONTINUED'))
                                       , default='open', max_length=255)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("commissions:commissions-detail", args=str(self.pk))


class Job(models.Model):
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)
    manpower_required = models.IntegerField()
    status = models.CharField(
        choices=(('open', 'OPEN'), ('full', 'FULL')), default='open', max_length=255)

    class Meta:
        ordering = [['open', 'full'], '-manpower_required', 'role']
    # entry=models.TextField()
    # created_on=models.DateTimeField(auto_now_add=True)
    # updated_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Job'


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(choices=(
        ('pending', 'PENDING'), ('accepted', 'ACCEPTED'), ('rejected', 'REJECTED')), default='pending', max_length=255)
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [['pending', 'accepted', 'rejected'], '-applied_on']


# Create your models here.
