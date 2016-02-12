# -*- encoding:utf8 -*-

from django.contrib import admin
from demo.models import Person, Group, Membership, Contact, SocialMedia


class SocialMediaAdmin(admin.StackedInline):
    model = SocialMedia

class ContactAdmin(admin.TabularInline):
    model = Contact

class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    list_per_page = 1
    inlines = [ContactAdmin, SocialMediaAdmin]

class MembershipAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_joined'


admin.site.register(Person, PersonAdmin)
admin.site.register(Group)
admin.site.register(Membership, MembershipAdmin)
