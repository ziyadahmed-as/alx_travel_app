from django.urls import path
from .views import ListOflocationsList, ListOfhotelsList, ListOfhotelsImagesList, ListOfhotelsReviewsList, ListOfhotelsBookingsList
    
 

urlpatterns = [
    path('locations/', ListOflocationsList.as_view(), name='location_list'),
    path('locations/<int:pk>/', ListOflocationsList.as_view(), name='location_detail'),
    path('hotels/', ListOfhotelsList.as_view(), name='hotel_list'),
    path('hotels/<int:pk>/', ListOfhotelsList.as_view(), name='hotel_detail'),
    path('hotels/<int:hotel_id>/images/', ListOfhotelsImagesList.as_view(), name='hotel_images_list'),
    path('hotels/<int:hotel_id>/images/<int:pk>/', ListOfhotelsImagesList.as_view(), name='hotel_image_detail'),
    path('hotels/<int:hotel_id>/reviews/', ListOfhotelsReviewsList.as_view(), name='hotel_reviews_list'),
    path('hotels/<int:hotel_id>/reviews/<int:pk>/', ListOfhotelsReviewsList.as_view(), name='hotel_review_detail'),
    path('hotels/<int:hotel_id>/bookings/', ListOfhotelsBookingsList.as_view(), name='hotel_bookings_list'),
]
