from django.urls import path
from . import views

app_name = 'photo'
urlpatterns = [
    # ex: /photo/
    path('', views.PhotoList.as_view(), name='index'),
    # ex: /photo/create/
    path('create/', views.PhotoCreate.as_view(), name='create'),
    # ex: /photo/delete/
    path('delete/<int:pk>/', views.PhotoDelete.as_view(), name='delete'),
    # ex: /photo/update/
    path('update/<int:pk>/', views.PhotoUpdate.as_view(), name='update'),
    # ex: /photo/detail/
    path('detail/<int:pk>/', views.PhotoDetail.as_view(), name='detail'),
]