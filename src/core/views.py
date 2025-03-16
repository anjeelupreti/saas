from django.shortcuts import render
from visits.models import PageVisit
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request, *args, **kwargs):
    context = {}
    return render(request, "dashboard.html", context)



def home(request, *args, **kwargs):
    # First, create the visit
    PageVisit.objects.create(path=request.path)

    # Now, calculate visits
    total_website_visits = PageVisit.objects.all().count()
    page_visits = PageVisit.objects.filter(path=request.path).count()

    # Calculate percentage safely
    try:
        percent = (page_visits * 100.0) / total_website_visits
    except ZeroDivisionError:
        percent = 0

    context = {
        "page_visit": page_visits,
        "percent_visit": percent,
        "total_website_visits": total_website_visits,
    }

    return render(request, "home.html", context)

