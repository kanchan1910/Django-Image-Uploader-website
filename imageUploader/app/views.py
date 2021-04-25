from django.shortcuts import render
from .models import Image
from .forms import ImageForm
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your photo has been uploaded!')
    form =ImageForm()
    img = Image.objects.all()
    return render(request,'index.html', {'img':img, 'form':form})
