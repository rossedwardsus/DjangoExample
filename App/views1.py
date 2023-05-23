from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    template = loader.get_template("index1.html")

    #return HttpResponse("Hello, world. You're at the polls index.")

    

    context = {
        "choice": request.POST["choice"]
    }

    return HttpResponse(template.render(context, request))

    #return render(request, "polls/detail.html", {"question": question})