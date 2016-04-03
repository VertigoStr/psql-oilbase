from django import template
from oilbase import models
import datetime

register = template.Library()


@register.inclusion_tag('oilbase/menu.html')
def menu(request):
	categories = models.Categories.objects.all().order_by("id")
	return {'categories':categories, 'path':request.path}

@register.inclusion_tag('oilbase/footer.html')
def footer():
	return {'year':datetime.datetime.now().year}

@register.inclusion_tag('oilbase/header.html')
def header():
	return {}