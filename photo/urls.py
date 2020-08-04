from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'photo'
urlpatterns = [
    path('', views.PhotoList.as_view(), name='index'),
    path('create/', views.PhotoCreate.as_view(), name='create'),
    path('delete/<int:pk>/', views.PhotoDelete.as_view(), name='delete'),
    path('update/<int:pk>/', views.PhotoUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.PhotoDetail.as_view(), name='detail'),
    path('like/<int:photo_id>/', views.PhotoLike.as_view(), name='like'),
    path('favorite/<int:photo_id>', views.Photofavorite.as_view(), name='favorite'),
    path('like/', views.PhotoLikeList.as_view(), name='like_list'),
    path('favorite/', views.PhotoFavoriteList.as_view(), name='favorite_list')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
