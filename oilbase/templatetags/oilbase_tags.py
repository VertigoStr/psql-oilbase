from django import template
from oilbase import models

register = template.Library()


@register.inclusion_tag('oilbase/menu.html')
def menu():
	categories = models.Categories.objects.all().order_by("id")
	return {'categories':categories}