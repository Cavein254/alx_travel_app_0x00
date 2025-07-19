from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from faker import Faker
import random
from datetime import timedelta

fake = Faker()

class Command(BaseCommand):
    help = 'Seeds the database with sample listings, bookings, and reviews'

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database...")

        # Clear existing data
        Review.objects.all().delete()
        Booking.objects.all().delete()
        Listing.objects.all().delete()

        listings = []
        for _ in range(100):
            available_from = fake.date_between(start_date='-30d', end_date='today')
            available_to = available_from + timedelta(days=random.randint(5, 30))

            listing = Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(),
                price_per_night=round(random.uniform(20, 500), 2),
                available_from=available_from,
                available_to=available_to
            )
            listings.append(listing)

        self.stdout.write("Created 100 listings.")

        # Create bookings
        bookings = []
        for _ in range(70):
            listing = random.choice(listings)
            start_date = fake.date_between(start_date=listing.available_from, end_date=listing.available_to - timedelta(days=2))
            end_date = start_date + timedelta(days=random.randint(1, 5))

            booking = Booking.objects.create(
                listing=listing,
                user=fake.name(),
                start_date=start_date,
                end_date=end_date
            )
            bookings.append(booking)

        self.stdout.write("Created 70 bookings.")

        # Create reviews
        for _ in range(100):
            listing = random.choice(listings)
            Review.objects.create(
                listing=listing,
                user=fake.name(),
                rating=random.randint(1, 5),
                comment=fake.sentence() if random.random() > 0.3 else ""
            )

        self.stdout.write(self.style.SUCCESS("Created 100 reviews. Seeding complete!"))
