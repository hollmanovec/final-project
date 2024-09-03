from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .models import Disc
from .forms import DiscForm, DiscSearchForm
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


class DiscDeleteView(DeleteView):
    model = Disc
    template_name = 'disc_delete_confirmation.html'
    success_url = reverse_lazy('disc_detail')


class DiscUpdateView(UpdateView):
    model = Disc
    form_class = DiscForm
    template_name = 'add_disc.html'
    success_url = reverse_lazy('disc_list')

def search_disc(request):
    if request.method == 'POST':
        form = DiscSearchForm(request.POST)
        if form.is_valid():
            disc_name = form.cleaned_data['disc_name']
            type = form.cleaned_data['type']
            object_list = Disc.objects.filter(name__icontains=disc_name, type__icontains=type)
            return render(request, 'search_disc_list.html', {'form': form, 'object_list': object_list})
    else:
        form = DiscSearchForm()
        object_list = Disc.objects.all()

    return render(request, 'search_disc_list.html', {'form': form, 'object_list': object_list})