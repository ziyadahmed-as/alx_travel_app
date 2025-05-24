from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import ListOflocations, ListOfhotels, ListOfhotelsImages, ListOfhotelsReviews, ListOfhotelsBookings
from .serializers import ListOflocationsSerializer, ListOfhotelsSerializer, ListOfhotelsImagesSerializer, ListOfhotelsReviewsSerializer, ListOfhotelsBookingsSerializer

class ListOflocationsViewSet(viewsets.ModelViewSet):
    queryset = ListOflocations.objects.all()
    serializer_class = ListOflocationsSerializer

    @action(detail=False, methods=['get'])
    def list_locations(self, request):
        locations = self.get_queryset()
        serializer = self.get_serializer(locations, many=True)
        return Response(serializer.data)
    @action(detail=True, methods=['get'])
    def retrieve_location(self, request, pk=None):
        location = self.get_object()
        serializer = self.get_serializer(location)
        return Response(serializer.data)
    @action(detail=False, methods=['post'])
    def create_location(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    @action(detail=True, methods=['put'])
    def update_location(self, request, pk=None):
        location = self.get_object()
        serializer = self.get_serializer(location, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    @action(detail=True, methods=['delete'])
    def delete_location(self, request, pk=None):
        location = self.get_object()
        location.delete()
        return Response(status=204)
    @action(detail=False, methods=['get'])
    def search_locations(self, request):
        query = request.query_params.get('q', None)
        if query:
            locations = self.get_queryset().filter(name__icontains=query)
        else:
            locations = self.get_queryset()
        serializer = self.get_serializer(locations, many=True)
        return Response(serializer.data)
    @action(detail=False, methods=['get'])
    def filter_locations(self, request):
        latitude = request.query_params.get('latitude', None)
        longitude = request.query_params.get('longitude', None)
        if latitude and longitude:
            locations = self.get_queryset().filter(latitude=latitude, longitude=longitude)
        else:
            locations = self.get_queryset()
        serializer = self.get_serializer(locations, many=True)
        return Response(serializer.data)
    @action(detail=False, methods=['get'])
    def sort_locations(self, request):
        sort_by = request.query_params.get('sort_by', 'name')
        locations = self.get_queryset().order_by(sort_by)
        serializer = self.get_serializer(locations, many=True)
        return Response(serializer.data)
    @action(detail=False, methods=['get'])
    def paginate_locations(self, request):
        page_size = request.query_params.get('page_size', 10)
        page_number = request.query_params.get('page_number', 1)
        locations = self.get_queryset()[(int(page_number)-1)*int(page_size):int(page_number)*int(page_size)]
        serializer = self.get_serializer(locations, many=True)
        return Response(serializer.data)
    @action(detail=False, methods=['get'])
    def count_locations(self, request):
        count = self.get_queryset().count()
        return Response({'count': count})
    @action(detail=False, methods=['get'])
    def aggregate_locations(self, request):
        from django.db.models import Avg, Max, Min, Count
        locations = self.get_queryset().aggregate(Avg('latitude'), Max('longitude'), Min('latitude'), Count('id'))
        return Response(locations)
    @action(detail=False, methods=['get'])
    def group_locations(self, request):
        from django.db.models import Count
        locations = self.get_queryset().values('name').annotate(count=Count('id'))
        return Response(locations)
    @action(detail=False, methods=['get'])
    def distinct_locations(self, request):
        locations = self.get_queryset().distinct('name')
        serializer = self.get_serializer(locations, many=True)
        return Response(serializer.data)
    
class ListOfhotelsViewSet(viewsets.ModelViewSet):
    queryset = ListOfhotels.objects.all()
    serializer_class = ListOfhotelsSerializer

    @action(detail=False, methods=['get'])
    def list_hotels(self, request):
        hotels = self.get_queryset()
        serializer = self.get_serializer(hotels, many=True)
        return Response(serializer.data)
    @action(detail=True, methods=['get'])
    def retrieve_hotel(self, request, pk=None):
        hotel = self.get_object()
        serializer = self.get_serializer(hotel)
        return Response(serializer.data)
    @action(detail=False, methods=['post'])
    def create_hotel(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    @action(detail=True, methods=['put'])
    def update_hotel(self, request, pk=None):
        hotel = self.get_object()
        serializer = self.get_serializer(hotel, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    @action(detail=True, methods=['delete'])
    def delete_hotel(self, request, pk=None):
        hotel = self.get_object()
        hotel.delete()
        return Response(status=204)
    @action(detail=False, methods=['get'])
    def search_hotels(self, request):
        query = request.query_params.get('q', None)
        if query:
            hotels = self.get_queryset().filter(name__icontains=query)
        else:
            hotels = self.get_queryset()
        serializer = self.get_serializer(hotels, many=True)
        return Response(serializer.data)
    @action(detail=False, methods=['get'])
    def filter_hotels(self, request):
        location_id = request.query_params.get('location_id', None)
        if location_id:
            hotels = self.get_queryset().filter(location_id=location_id)
        else:
            hotels = self.get_queryset()
        serializer = self.get_serializer(hotels, many=True)
        return Response(serializer.data)
    @action(detail=False, methods=['get'])
    def sort_hotels(self, request):
        sort_by = request.query_params.get('sort_by', 'name')
        hotels = self.get_queryset().order_by(sort_by)
        serializer = self.get_serializer(hotels, many=True)
        return Response(serializer.data)
    @action(detail=False, methods=['get'])
    def paginate_hotels(self, request):
        page_size = request.query_params.get('page_size', 10)
        page_number = request.query_params.get('page_number', 1)
        hotels = self.get_queryset()[(int(page_number)-1)*int(page_size):int(page_number)*int(page_size)]
        serializer = self.get_serializer(hotels, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def count_hotels(self, request):
        count = self.get_queryset().count()
        return Response({'count': count})
    @action(detail=False, methods=['get'])
    def aggregate_hotels(self, request):
        from django.db.models import Avg, Max, Min, Count
        hotels = self.get_queryset().aggregate(Avg('price_per_night'), Max('price_per_night'), Min('price_per_night'), Count('id'))
        return Response(hotels)
    @action(detail=False, methods=['get'])
    def group_hotels(self, request):
        from django.db.models import Count
        hotels = self.get_queryset().values('location__name').annotate(count=Count('id'))
        return Response(hotels)
    @action(detail=False, methods=['get'])
    def distinct_hotels(self, request):
        hotels = self.get_queryset().distinct('name')
        serializer = self.get_serializer(hotels, many=True)
        return Response(serializer.data)

class ListOfhotelsImagesViewSet(viewsets.ModelViewSet):
    queryset = ListOfhotelsImages.objects.all()
    serializer_class = ListOfhotelsImagesSerializer

    @action(detail=False, methods=['get'])
    def list_images(self, request):
        images = self.get_queryset()
        serializer = self.get_serializer(images, many=True)
        return Response(serializer.data)
    @action(detail=True, methods=['get'])
    def retrieve_image(self, request, pk=None):
        image = self.get_object()
        serializer = self.get_serializer(image)
        return Response(serializer.data)
    @action(detail=False, methods=['post'])
    def create_image(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    @action(detail=True, methods=['put'])
    def update_image(self, request, pk=None):
        image = self.get_object()
        serializer = self.get_serializer(image, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    @action(detail=True, methods=['delete'])
    def delete_image(self, request, pk=None):
        image = self.get_object()
        image.delete()
        return Response(status=204)
    @action(detail=False, methods=['get'])
    def search_images(self, request):
        query = request.query_params.get('q', None)
        if query:
            images = self.get_queryset().filter(hotel__name__icontains=query)
        else:
            images = self.get_queryset()
        serializer = self.get_serializer(images, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def filter_images(self, request):
        hotel_id = request.query_params.get('hotel_id', None)
        if hotel_id:
            images = self.get_queryset().filter(hotel_id=hotel_id)
        else:
            images = self.get_queryset()
        serializer = self.get_serializer(images, many=True)
        return Response(serializer.data)
    
class ListOfhotelsReviewsViewSet(viewsets.ModelViewSet):
    queryset = ListOfhotelsReviews.objects.all()
    serializer_class = ListOfhotelsReviewsSerializer

    @action(detail=False, methods=['get'])
    def list_reviews(self, request):
        reviews = self.get_queryset()
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)
    @action(detail=True, methods=['get'])
    def retrieve_review(self, request, pk=None):
        review = self.get_object()
        serializer = self.get_serializer(review)
        return Response(serializer.data)
    @action(detail=False, methods=['post'])
    def create_review(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    @action(detail=True, methods=['put'])
    def update_review(self, request, pk=None):
        review = self.get_object()
        serializer = self.get_serializer(review, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    @action(detail=True, methods=['delete'])
    def delete_review(self, request, pk=None):
        review = self.get_object()
        review.delete()
        return Response(status=204)
    @action(detail=False, methods=['get'])
    def search_reviews(self, request):
        query = request.query_params.get('q', None)
        if query:
            reviews = self.get_queryset().filter(hotel__name__icontains=query)
        else:
            reviews = self.get_queryset()
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)
    @action(detail=False, methods=['get'])
    def filter_reviews(self, request):
        hotel_id = request.query_params.get('hotel_id', None)
        if hotel_id:
            reviews = self.get_queryset().filter(hotel_id=hotel_id)
        else:
            reviews = self.get_queryset()
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)