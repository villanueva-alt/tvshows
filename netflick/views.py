from django.shortcuts import render
from .models import Show
from .forms import ShowForm

def home(request):
    #get count of how many shows
    show_count = Show.objects.all().count()

    ctx = {
        "show_count": show_count
    }

    return render(request, "home.html", context=ctx)

def new_show(request):
    
    ctx = {
        "forms": None
    }

    if request.method == "POST":
        #TODO do the create here
        pass
    else:
        ctx["forms"] = ShowForm()
    
    return render(request, "new_show.html", context=ctx)



def all_shows(request):
    
    shows = Show.objects.all()
    
    context = {
        "shows": shows
    }

    return render(request, "all_shows.html", context=context)

def get_show(request, show_id):

    show = Show.objects.get(pk=show_id)

    context = {
        "show": show
    }

    return render(request, "show.html", context=context)
