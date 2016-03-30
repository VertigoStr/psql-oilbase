from django.shortcuts import render
from . import models

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
	main_persons = models.Personal.objects.filter(departament='2')
	send_persons = models.Personal.objects.filter(departament='1')
	callback = models.CallBack.objects.all()
	return render(request, 'oilbase/contacts.html', {'contacts':contacts, 'departs':departs, 'main_persons':main_persons, 'send_persons':send_persons, 'callback':callback})	

def contacts_callback(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.name = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('oilbase.views.contacts_page', pk = post.pk)
	else:
		form = PostForm()

	return render(request, 'oilbase/contacts.html', {'form':form})