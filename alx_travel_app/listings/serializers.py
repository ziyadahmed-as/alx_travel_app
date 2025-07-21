
from rest_framework import serializers
from .models import ListOflocations, ListOfhotels, ListOfhotelsImages, ListOfhotelsReviews, ListOfhotelsBookings

class ListOflocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListOflocations
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': True},
            'latitude': {'required': True},
            'longitude': {'required': True},
        }
        
class ListOfhotelsSerializer(serializers.ModelSerializer):
    location = ListOflocationsSerializer(read_only=True)
    
    class Meta:
        model = ListOfhotels
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'name': {'required': True},
            'location': {'required': True},
            'description': {'required': True},
            'price_per_night': {'required': True},
        }
class ListOfhotelsImagesSerializer(serializers.ModelSerializer):
    hotel = ListOfhotelsSerializer(read_only=True)
    
    class Meta:
        model = ListOfhotelsImages
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'hotel': {'required': True},
            'image': {'required': True},
        }
class ListOfhotelsReviewsSerializer(serializers.ModelSerializer):
    hotel = ListOfhotelsSerializer(read_only=True)
    
    class Meta:
        model = ListOfhotelsReviews
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'hotel': {'required': True},
            'user': {'required': True},
            'rating': {'required': True},
            'comment': {'required': True},
        }
        
class ListOfhotelsBookingsSerializer(serializers.ModelSerializer):
    hotel = ListOfhotelsSerializer(read_only=True)
    
    class Meta:
        model = ListOfhotelsBookings
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'hotel': {'required': True},
            'user': {'required': True},
            'check_in_date': {'required': True},
            'check_out_date': {'required': True},
            'number_of_guests': {'required': True},
        }
# The serializers above are used to convert complex data types, such as querysets and model instances, into native Python datatypes that can then be easily rendered into JSON or XML.