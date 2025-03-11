from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Orchestra


# Create your views here.

class OrchestraList(generic.ListView):
    """
    Returns all Orchestras in :model:`start.Orchestra`
    **Context**

    ``queryset``
        All instances of :model:`start.Orchestra`

    **Template:**

    :template:`start/index.html`
    """
    queryset = Orchestra.objects.all()
    template_name = "start/index.html"