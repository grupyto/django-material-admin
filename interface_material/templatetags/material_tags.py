# -*-coding:utf-8 -*-
from django import template
from django.forms import CheckboxInput

register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter(name='addstyle')
def addstyle(field, style):
   return field.as_widget(attrs={"style": style})


@register.filter(name='addCssStyle')
def addCssStyle(field, args):
    if args:
        css, style = args.split(",")
        return field.as_widget(attrs={"class": css, "style": style})


@register.filter(name='disabled')
def disabled(field):
   return field.as_widget(attrs={"disabled"})


@register.filter(name='is_checkbox')
def is_checkbox(field):
  return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__