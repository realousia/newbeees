from django.shortcuts import render
from .models import Honeycomb as hc

# Create your views here.
def index(request):
	hc_list = hc.objects.all()
	return render(request, 'poster/index.html', {
		'hc_list': hc_list,
	})

def new_honey(request):
	return render(request, 'poster/honey_form.html')