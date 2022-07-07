from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('add', views.addPage, name="addpage"),
    path('edit/<id>', views.editPage, name="editpage"),
    path('page/create', views.savePage, name="create_page"),
    path('editPage/<id>', views.editPageContent, name="editPageContent"),
    path('preview/<id>', views.previewPage, name='previewPage')
]
