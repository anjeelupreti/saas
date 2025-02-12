from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit




def home_view(request , *args, **kwargs):
    total_website_visits=PageVisit.objects.all().count()
    page_visits=PageVisit.objects.filter(path=request.path).count()
    try:
        percent=(page_visits*100.0)/total_website_visits
    except:
        percent=0
    context={
        # "page_title":title,
        "page_visit":page_visits,
        "percent_visit":percent,
        "total_website_visits":total_website_visits,


        
    }
    PageVisit.objects.create(path=request.path)
    return render(request ,"home.html", context)