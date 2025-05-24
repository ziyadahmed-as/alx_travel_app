from django.db import models

# Create your models here
class ListOflocations(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('location_detail', args=[str(self.id)])
    
    
class ListOfhotels(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(ListOflocations, on_delete=models.CASCADE)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    def __str__(self):
        return self.name
    
class ListOfhotelsImages(models.Model):
    hotel = models.ForeignKey(ListOfhotels, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='hotel_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image for {self.hotel.name}"
    
class ListOfhotelsReviews(models.Model):
    hotel = models.ForeignKey(ListOfhotels, on_delete=models.CASCADE, related_name='reviews')
    user = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review for {self.hotel.name} by {self.user}"

class ListOfhotelsBookings(models.Model):
    hotel = models.ForeignKey(ListOfhotels, on_delete=models.CASCADE, related_name='bookings')
    user = models.CharField(max_length=100)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_guests = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking for {self.hotel.name} by {self.user}"
    
