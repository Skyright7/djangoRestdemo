from django.urls import path
from peprclip import views

app_name = 'peprclip'

urlpatterns = [
    path('', views.function_list, name='function list'),
    path('<int:pk>/', views.function_detail_list.as_view(), name='function detail'),
]