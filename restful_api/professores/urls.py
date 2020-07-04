from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProfessorList.as_view(), name='professor_list'),
    path('view/<int:pk>', views.ProfessorView.as_view(), name='professor_view'),
    path('new', views.ProfessorCreate.as_view(), name='professor_new'),
    path('edit/<int:pk>', views.ProfessorUpdate.as_view(), name='professor_edit'),
    path('delete/<int:pk>', views.ProfessorDelete.as_view(), name='professor_delete'),
]
