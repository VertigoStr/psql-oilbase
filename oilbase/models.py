from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
import os

# Create your models here.
class Dilers(models.Model):
	city = models.CharField(max_length=50, verbose_name='Область')
	address = models.CharField(max_length=250, verbose_name='Адрес')
	phone = models.CharField(max_length=20, verbose_name='Телефон')
	coordinats = models.CharField(max_length=100, verbose_name='Координаты', null=True)
	email = models.EmailField(verbose_name='Почта')

	class Meta:
		verbose_name = u'Дилеры'
		verbose_name_plural = u'Дилеры'


class Deliver(models.Model):
	title = models.CharField(max_length=100, verbose_name='Имя')
	description = models.TextField(verbose_name='Описание')
	first_image = models.ImageField(upload_to=u'./media/img/', verbose_name='Изображение №1')
	second_image = models.ImageField(upload_to=u'./media/img/', verbose_name='Изображение №2')
	third_image = models.ImageField(upload_to=u'./media/img/', verbose_name='Изображение №3')

	class Meta:
		verbose_name = u'Поставка'
		verbose_name_plural = u'Поставки'

	def img_first(self):
		if self.first_image:
			return '<img src="%s" width="100"/>' % self.first_image.url
		else:
			return '(none)'
	img_first.short_description = 'Изображение №1'
	img_first.allow_tags = True

	def img_second(self):
		if self.second_image:
			return '<img src="%s" width="100"/>' % self.second_image.url
		else:
			return '(none)'

	img_second.short_description = 'Изображение №2'
	img_second.allow_tags = True

	def img_third(self):
		if self.third_image:
			return '<img src="%s" width="100"/>' % self.third_image.url
		else:
			return '(none)'

	img_third.short_description = 'Изображение №3'
	img_third.allow_tags = True

	def __str__(self):
		return self.title


class Categories(models.Model):
	title = models.CharField(max_length=100, verbose_name='Имя')
	description = models.TextField(verbose_name='Описание')
	
	class Meta:
		verbose_name = u'Категории'
		verbose_name_plural = u'Категории'	

	def __str__(self):
		return self.title


class Products(models.Model):
	title = models.CharField(max_length=100, verbose_name='Имя')
	image = models.ImageField(upload_to=u'./media/img/', verbose_name='Изображение')
	description = models.CharField(max_length=250, verbose_name='Описание')
	content = models.CharField(max_length=100, verbose_name='Емкость')
	gost = models.CharField(max_length=250, verbose_name='ГОСТ')
	docs = models.CharField(max_length=250, verbose_name='Паспорт качества')
	cost = models.IntegerField(verbose_name='Цена')
	send_type = models.ForeignKey('Deliver', on_delete=models.CASCADE, verbose_name='Тип доставки')
	category = models.ForeignKey('Categories', on_delete=models.CASCADE, verbose_name='Категория')

	class Meta:
		verbose_name = u'Товар'
		verbose_name_plural = u'Товары'

	def img(self):
		if self.image:
			return '<img src="%s" width="100"/>' % self.image.url
		else:
			return '(none)'
	img.short_description = 'Изображение'
	img.allow_tags = True

class Departaments(models.Model):
	title = models.CharField(max_length=100, verbose_name='Имя')
	worktime = ArrayField(models.CharField(max_length=15), blank=True, size=7, verbose_name='График работы')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = u'Отдел'
		verbose_name_plural = u'Отделы'

class Personal(models.Model):
	name = models.CharField(max_length=200, verbose_name='Имя')
	post = models.CharField(max_length=100, verbose_name='Должность')
	phone = models.CharField(max_length=20, verbose_name='Телефон')
	email = models.EmailField(verbose_name='Почта')
	departament = models.ForeignKey('Departaments', on_delete=models.CASCADE, verbose_name='Отдел')

	class Meta:
		verbose_name = u'Персонал'
		verbose_name_plural = u'Персонал'

class CallBack(models.Model):
	name = models.CharField(max_length=200, verbose_name='Имя')
	phone = models.CharField(max_length=20, verbose_name='Телефон')
	email = models.EmailField(verbose_name='Почта')
	message = models.TextField(verbose_name='Сообщение')

	class Meta:
		verbose_name = u'Обратная связь'
		verbose_name_plural = u'Обратная связь'

class Slogans(models.Model):
	title = models.CharField(max_length=100, verbose_name='Имя')
	description = models.TextField(verbose_name='Описание')
	page = models.CharField(max_length=100, verbose_name='Страница', null=True)

	class Meta:
		verbose_name = u'Слоган'
		verbose_name_plural = u'Слоганы'

class Contact(models.Model):
	name = models.CharField(max_length=100, verbose_name='Имя')
	address = models.CharField(max_length=250, verbose_name='Адрес')
	coordinats = models.CharField(max_length=100, verbose_name='Координаты', null=True)
	site = models.CharField(max_length=20, verbose_name='Сайт')
	email = models.EmailField(verbose_name='Адрес электронной почты')

	class Meta:
		verbose_name = u'Контакт'
		verbose_name_plural = u'Контакты'

class MainPageContent(models.Model):
	title = models.CharField(max_length=100, verbose_name='Имя')
	description = models.TextField(verbose_name='Описание')
	img = models.ImageField(upload_to=u'./media/img/', verbose_name='Изображение', null=True)

	def image(self):
		if self.img:
			return '<img src="%s" width="100"/>' % self.img.url
		else:
			return '(none)'
	image.short_description = 'Изображение'
	image.allow_tags = True
	
	class Meta:
		verbose_name = u'Элемент'
		verbose_name_plural = u'Элементы'
