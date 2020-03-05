from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.IndexView.as_view(), name = "index"),
    path('<slug:slug>/', views.IndexView.as_view(), name='category'),

    # path('<int:event_id>/', views.detail, name='detail'),
]
