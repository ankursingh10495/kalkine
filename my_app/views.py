from django.shortcuts import render
from my_app.models import CardDetail
from django.http import JsonResponse
import json
# Create your views here.

def first_page(request):
	pass

	return render(request, 'index.html')


def add_card(request):
	if request.method == 'POST':
		form = request.POST
		card_title = form.get('card_title')
		card_text = form.get('card_text')

		print(card_title)
		print(card_text)

		add = CardDetail.objects.create(card_title=card_title,
								        card_text=card_text)

		if add:
			data_json = {
				'id': 1,
				'msg': 'Added'
			}
		else:
			data_json = {
				'id': 0,
				'msg': 'Somwthing went wrong'
			}

		return JsonResponse(data_json)


def get_data_list(request):
	if request.method == 'GET':
		get_data = CardDetail.objects.all()
		data_list = []
		if get_data:
			for obj in get_data:
				data_dict = {}
				data_dict['id'] = obj.id
				data_dict['card_title'] = obj.card_title
				data_dict['card_text'] = obj.card_text

				data_list.append(data_dict)

		return JsonResponse(data_list, safe=False)


def delete_card(request):
	if request.method == 'GET':
		get_id = request.GET.get('card')

		check_card = CardDetail.objects.filter(pk=get_id)
		if check_card:
			CardDetail.objects.filter(pk=get_id).delete()

			data_json = {
				'id': 1,
				'msg': 'Deleted Successfully'
			}
		else:
			data_json = {
				'id': 0,
				'msg': 'Somwthing went wrong'
			}

		return JsonResponse(data_json)