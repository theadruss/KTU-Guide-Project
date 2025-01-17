from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('susbscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),
    path('scheme2019/', views.scheme2019, name='scheme2019'),
    path('scheme2024/', views.scheme2024, name='scheme2024'),
    path('linkpage/<int:semester_id>/', views.linkpage, name='linkpage'),
    path('sempage/<int:branch_id>/', views.sempage, name='sempage'),
    path('results/', views.results, name='results'),
    path('updates/', views.updates, name='updates'),
]