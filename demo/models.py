from django.db import models

class Contact(models.Model):
    cell_phone = models.CharField(max_length=20)
    twitter = models.CharField(max_length=20)
    address = models.TextField(null=True, blank=True)
    person = models.ForeignKey('Person')

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    picture = models.FileField(upload_to='person', null=True, blank=True)

    def __unicode__(self):
        return self.first_name

class Permissions(models.Model):
    name = models.CharField(max_length=100)
    enabled = models.BooleanField(default=True)


class Group(models.Model):
    name = models.CharField(max_length=128)
    permissions = models.ManyToManyField(Permissions)
    members = models.ManyToManyField(Person, through='Membership')


class Membership(models.Model):
    person = models.ForeignKey(Person)
    group = models.ForeignKey(Group)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
