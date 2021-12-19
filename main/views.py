from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import services
from .forms import ContactForm


def main_view(request):
    return render(request, 'main/main_view.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            services.send_message(form.cleaned_data)
            return HttpResponseRedirect(reverse('contact'))
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})