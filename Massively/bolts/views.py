from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'bolts/index.html'

class GenericView(TemplateView):
    template_name = 'bolts/generic.html'

class ElementsView(TemplateView):
    template_name = 'bolts/elements.html'
