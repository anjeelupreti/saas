from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit




def home_page_view(request , *args, **kwargs):
    
    context={
        
    }
    PageVisit.objects.create()
    return render(request ,"home.html", context)