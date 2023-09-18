from django.urls import path
from . import views


urlpatterns = [
    path('',views.homepage),
    path('gold',views.gold),
    path('silver',views.silver),
]
