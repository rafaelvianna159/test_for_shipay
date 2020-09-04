from django.urls import path

from . import views

urlpatterns = [
    path('transacao', views.transacao, name='transacao'),
    path('transacao/estabelecimento',views.transacao, name='transacao')
]