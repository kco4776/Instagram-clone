from django.urls import path
from . import views

app_name = 'photo'
urlpatterns = [
    # ex: /photo/
    path('', views.PhotoList.as_view(), name='list'),
    # ex: /photo/create/
    path('create/', views.PhotoCreate.as_view(), name='create'),
    # ex: /photo/delete/
    path('delete/<int:pk>/', views.PhotoDelete.as_view(), name='delete'),
    # ex: /photo/update/
    path('update/<int:pk>/', views.PhotoUpdate.as_view(), name='update'),
    # ex: /photo/detail/
    path('detail/<int:pk>/', views.PhotoDetail.as_view(), name='detail'),
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
