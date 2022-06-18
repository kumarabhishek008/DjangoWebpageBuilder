from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('page/create', views.savePage, name="create_page")
]
