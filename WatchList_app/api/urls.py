from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (WatchDetailAV, ReviewList, UserReview, ReviewDetail,
                    WatchListAV, ReviewCreate, StreamPlatformVS, WatchLists, StreamPlatformAV
                    )

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('list2/', WatchLists.as_view(), name='watch-list'),
    path('list/<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),

    path('', include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),

    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail')

    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('review/<str:username>/', UserReview.as_view(), name='user-review-detail'),
    path('review/', UserReview.as_view(), name='user-review-detail'),
]
