from django.shortcuts import render
from .models import Honeycomb as hc
from .models import Honey as h
from .models import Flower as f 
from el_pagination.decorators import page_template

# Create your views here.
@page_template('poster/entry_list.html')
def index(request, 
	template='poster/index.html',
	extra_context=None):
	hc_list = hc.objects.all()
	h_list = h.objects.all().order_by('-id')
	
	context = {
	    'hc_list': hc_list,
		'h_list': h_list,
	}
	if extra_context is not None:
		context.update(extra_context)
	return render(request, template, context)

def honey_list(request, pk):
	hc_list = hc.objects.all()
	honey = h.objects.get(pk=pk)
	flower = honey.flowers.all()
	return render(request, 'poster/honey_list.html', {
		'honey': honey,
		'flower': flower,
		'hc_list': hc_list,
	})
	
@page_template('poster/entry_list.html')
def honeycomb_detail(request, honeycomb, 
	template='poster/honeycomb_detail.html', 
	extra_context=None):
	hc_list = hc.objects.all()
	h_list = h.objects.filter(honeycomb__name=honeycomb.upper()).order_by('-id')
	
	context = {
	    'hc_list': hc_list,
		'h_list': h_list,
	}
	if extra_context is not None:
		context.update(extra_context)
	return render(request, template, context)

def new_honey(request):
	return render(request, 'poster/honey_form.html')

def about(request):
	hc_list = hc.objects.all()
	return render(request, 'poster/about.html', {
		'hc_list': hc_list,	
	})
	