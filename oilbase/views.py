from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from . import models
from .forms import CallBackForm

# Create your views here.
def main_page(request):
	content = models.MainPageContent.objects.all()
	carousel = models.Slogans.objects.filter(page='Главная')
	return render(request, 'oilbase/main.html', {'content':content, 'carousel':carousel})

def delivery_page(request):
	carousel = models.Slogans.objects.filter(page='Доставка')
	content = models.Deliver.objects.all()
	return render(request, 'oilbase/delivery.html', {'content':content, 'carousel':carousel})

def dilers_page(request):
	dilers = models.Dilers.objects.all()
	return render(request, 'oilbase/dilers.html', {'dilers':dilers})	

def contacts_page(request):
	contacts = models.Contact.objects.all()
	departs = models.Departaments.objects.all()
	main_persons = models.Personal.objects.filter(departament='1')
	send_persons = models.Personal.objects.filter(departament='2')
	callback = models.CallBack.objects.all()

	if request.method == "POST":
		form = CallBackForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.name =  form.cleaned_data['name']
			post.email = form.cleaned_data['email']
			post.phone =  form.cleaned_data['phone']
			post.message =  form.cleaned_data['message']
			post.save()
			return HttpResponseRedirect('contacts')
	else:
		form = CallBackForm()

	return render(request, 'oilbase/contacts.html', {'contacts':contacts, 'departs':departs, 'main_persons':main_persons, 'send_persons':send_persons, 'callback':callback, 'form':form})	


def products_page(request, pk="1"):
	categories = models.Categories.objects.all().order_by("id")
	
	length = len(categories)
	if int(pk) in range(1, length + 1):
		next_el = int(pk) + 1
		if next_el > length:
			next_el = 1
		prev_el = int(pk) - 1
		if prev_el < 1:
			prev_el = length

	indexes = {'current':int(pk), 'next':int(next_el), 'prev':int(prev_el)}
	products = models.Products.objects.filter(category=pk)

	return render(request, 'oilbase/products.html', {'products':products, 'categories':categories, 'item':indexes})