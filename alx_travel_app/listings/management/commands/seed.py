# listings/management/commands/seed.py

from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker
import random
from datetime import timedelta, date

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding listings...")

        # Delete old entries if needed:
        Listing.objects.all().delete()

        listings = []
        for _ in range(200):
            start_date = fake.date_between(start_date='today', end_date='+30d')
            end_date = start_date + timedelta(days=random.randint(1, 14))

            listing = Listing(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=5),
                price_per_night=round(random.uniform(20, 500), 2),
                available_from=start_date,
                available_to=end_date,
            )
            listings.append(listing)

        Listing.objects.bulk_create(listings)
        self.stdout.write(self.style.SUCCESS('Successfully seeded 200+ listings.'))
