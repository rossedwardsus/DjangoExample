from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from rest_framework.response import JsonResponse


# Create your views here.


def index(request):
    template = loader.get_template("index.html")

    #return HttpResponse("Hello, world. You're at the polls index.")

    context = {}

    return HttpResponse(template.render(context, request))

    #return render(request, "polls/detail.html", {"question": question})


@api_view(['GET', 'PUT', 'DELETE'])
def api_view_test(request):

    return Response({"test": "test"})