from django.shortcuts import render
from .models import Honeycomb as hc
from .models import Honey as h
from .models import Flower as f 

# Create your views here.
def index(request):
	hc_list = hc.objects.all()
	h_list = h.objects.all()
	return render(request, 'poster/index.html', {
		'hc_list': hc_list,
		'h_list': h_list,
	})

def honey_list(request, pk):
	hc_list = hc.objects.all()
	honey = h.objects.get(pk=pk)
	flower = honey.flowers.all()
	return render(request, 'poster/honey_list.html', {
		'honey': honey,
		'flower': flower,
		'hc_list': hc_list,
	})

def honeycomb_detail(request, honeycomb):
	hc_list = hc.objects.all()
	honey = h.objects.filter(honeycomb__name=honeycomb.upper())
	return render(request, 'poster/honeycomb_detail.html', {
		'honey': honey,
		'hc_list': hc_list,
	})

def new_honey(request):
	return render(request, 'poster/honey_form.html')

def about(request):
	hc_list = hc.objects.all()
	return render(request, 'poster/about.html', {
		'hc_list': hc_list,	
	})