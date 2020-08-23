from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Application
from .serializers import ApplicationSerializer
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
class ApplicationList(APIView):

    def get(self, request):
        apps = Application.objects.all()
        serialilzer = ApplicationSerializer(apps, many=True)
        return Response(serialilzer.data)

    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    data = Application.objects.all()
    context = {
        'all_data': data
    }
    return render(request, 'index.html', context)


def details(request):
    email = request.GET.get("email")
    if email:
        print(email)
        data = Application.objects.filter(pk=email)
        context = {
            'all_data': data
        }
        return render(request, 'details.html', context)
    return HttpResponse("<h1> Sorry Invalid URL </h1>")


@csrf_exempt
def update(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        notes = request.POST.get("note")
        print(notes)
        if Application.objects.filter(pk=email).update(notes=notes):
            return HttpResponse("Successfully updated")


@xframe_options_exempt
def apply(request):
    return render(request, 'apply_form.html')