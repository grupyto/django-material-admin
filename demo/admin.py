# -*- encoding:utf8 -*-

from django.contrib import admin
from demo.models import Person, Group, Membership, Contact

class ContactAdmin(admin.StackedInline):
    model = Contact

class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    list_per_page = 1
    inlines = [ContactAdmin, ]

class MembershipAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_joined'


admin.site.register(Person, PersonAdmin)
admin.site.register(Group)
admin.site.register(Membership, MembershipAdmin)
