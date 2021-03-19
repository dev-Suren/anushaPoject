from django.urls import path
from. import views

urlpatterns = [
	path('addJob',views.addJob, name='addJob'),
	
]