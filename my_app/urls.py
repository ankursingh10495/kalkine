from django.urls import path
from my_app import views

app_name = 'my_app'

urlpatterns = [
	path('', views.first_page, name='first_page'),
	path('add_card/', views.add_card, name='add_card'),
	path('get_data_list/', views.get_data_list, name='get_data_list'),
	path('delete_card/', views.delete_card, name='delete_card'),
]