from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from . import models

# Register your models here.

class Dilers(admin.ModelAdmin):
    list_display = ('city', 'address', 'phone', 'coordinats', 'email',)
    ordering = ('city',)

admin.site.register(models.Dilers, Dilers)

class Deliver(admin.ModelAdmin):
	list_display = ('title', 'description', 'img_first', 'img_second', 'img_third',)
	ordering = ('title',)

admin.site.register(models.Deliver, Deliver)

class Categories(admin.ModelAdmin):
	list_display = ('title', 'description',)
	ordering = ('title',)

admin.site.register(models.Categories, Categories)

class Products(admin.ModelAdmin):
	list_display = ('title', 'img', 'description', 'send_type', 'content', 'gost', 'docs', 'cost', 'category',)
	list_filter = ['category', ]
	ordering = ('title',)

admin.site.register(models.Products, Products)

class Departaments(admin.ModelAdmin):
	list_display = ('title', 'worktime')
	ordering = ('title',)

admin.site.register(models.Departaments, Departaments)

class Personal(admin.ModelAdmin):
	list_display = ('name', 'post', 'phone', 'email', 'departament',)
	list_filter = ['departament', ]
	ordering = ('name',)

admin.site.register(models.Personal, Personal)

class CallBack(admin.ModelAdmin):
	list_display = ('name', 'phone', 'email', 'message',)
	ordering = ('name',)

admin.site.register(models.CallBack, CallBack)

class Slogans(admin.ModelAdmin):
	list_display = ('title', 'description', 'page',)
	list_filter = ['page', ]
	ordering = ('title',)

admin.site.register(models.Slogans, Slogans)

class Contact(admin.ModelAdmin):
	list_display = ('name', 'address', 'coordinats', 'email', 'site',)
	ordering = ('name',)

admin.site.register(models.Contact, Contact)

class MainPageContent(admin.ModelAdmin):
	list_display = ('title', 'description', 'image')
	ordering = ('title',)

admin.site.register(models.MainPageContent, MainPageContent)