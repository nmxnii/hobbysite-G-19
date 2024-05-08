from django.db import models
from django.urls import reverse
from user_management.models import *


class Commission(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=(('open', 'OPEN'), ('full', 'FULL'),
                                       ('completed', 'COMPLETED'), ('discontinued', 'DISCONTINUED')), default='open', max_length=255)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("commissions:commissions-detail", kwargs={"pk": (self.pk)})


class Job(models.Model):
    commission = models.ForeignKey(
        Commission, on_delete=models.CASCADE, related_name="jobs")
    role = models.CharField(max_length=255)
    manpower_required = models.IntegerField()
    status = models.CharField(
        choices=(('open', 'OPEN'), ('full', 'FULL')), default='open', max_length=255)

    class Meta:
        ordering = ['-status', '-manpower_required', 'role']
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Job ' + str(self.pk) + ": " + str(self.commission) + ': ' + self.role


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE,
                            related_name="applicants")
    applicant = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.CharField(choices=(
        ('pending', 'PENDING'), ('accepted', 'ACCEPTED'), ('rejected', 'REJECTED')), default='pending', max_length=255)
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['status', '-applied_on']

    def __str__(self):
        return str(self.applicant) + ' applying for ' + str(self.job.role)


# Create your models here.
