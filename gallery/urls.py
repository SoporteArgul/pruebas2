from django.urls import path
from . import views
app_name = 'gallery'
urlpatterns = [
    path('upload_image/', views.upload_image, name='upload_image')]