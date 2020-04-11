from django.urls import path
from core import views as view


urlpatterns = [
    path('', view.home, name='home'),
    path('create/', view.create, name='create'),
    path('vote/<int:pk>/', view.vote, name='vote'),
    path('result/<int:pk>/', view.result, name='result'),
]
