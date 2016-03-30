from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.main_page, name='main_page'),
	url(r'^delivery$', views.delivery_page, name='delivery_page'),
	url(r'^dilers$', views.dilers_page, name='dilers_page'),
	url(r'^contacts$', views.contacts_page, name='contacts_page'),
]