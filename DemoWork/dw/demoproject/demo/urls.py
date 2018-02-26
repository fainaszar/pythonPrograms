from django.conf.urls import url

from . import views

urlpatterns=[

	url(r'^$',views.home,name='home'),
	url(r'^upload/$',views.model_form_upload,name='upload'),
	url(r'^charts/$', views.chart, name = 'charts'),
]