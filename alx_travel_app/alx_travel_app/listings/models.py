from django.db import models

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available_from = models.DateField()
    available_to = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Listing'
        verbose_name_plural = 'Listings'
        constraints = [
            models.CheckConstraint(
                check=models.Q(available_from__lt=models.F('available_to')),
                name='available_from_before_available_to'
            )
        ]

class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)  # Assuming a simple string for user, can be replaced with a User model
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Booking for {self.listing.title} by {self.user}"
    class Meta:
        ordering = ['start_date']
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        constraints = [
            models.CheckConstraint(
                check=models.Q(start_date__lt=models.F('end_date')),
                name='start_date_before_end_date'
            )
        ]   

class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)  # Assuming a simple string for user, can be replaced with a User model
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Review for {self.listing.title} by {self.user}"

    class Meta:
        ordering = ['-rating']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        constraints = [
            models.CheckConstraint(
                check=models.Q(rating__gte=1) & models.Q(rating__lte=5),
                name='rating_between_1_and_5'
            )
        ]