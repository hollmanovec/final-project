from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Disc
from .forms import DiscForm
#from .forms import DiscSearchForm
from django.shortcuts import render


# Create your views here.


class DiscCreateView(CreateView):
    model = Disc
    form_class = DiscForm
    template_name = "add_disc.html"
    success_url = reverse_lazy('add_disc')


class DiscListView(ListView):
    model = Disc
    template_name = 'pagination_discs.html'
    context_object_name = 'discs'
    paginate_by = 5


class DiscDetailView(DetailView):
    model = Disc
    template_name = 'disc_detail.html'

