from django.shortcuts import render

# Create your views here.

def upload_image(request):
   if request.method == 'GET':
      return render(request, 'upload_image.html')