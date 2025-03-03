import csv
from django.core.management.base import BaseCommand
from recommender.models import Brand, Shoe

class Command(BaseCommand):
    help = "Import running shoe data from CSV"

    def handle(self, *args, **kwargs):
        file_path = "shoes_data.csv"

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                brand, _ = Brand.objects.get_or_create(name=row["brand"])
                Shoe.objects.create(
                    brand=brand,
                    model=row["model"],
                    category=row["category"],
                    weight=float(row["weight"]),
                    drop=float(row["drop"]),
                    pronation=row["pronation"],
                    cushioning=row["cushioning"],
                    terrain=row["terrain"],
                    plate=row["plate"].lower() == "true"
                )

        self.stdout.write(self.style.SUCCESS("Shoe data imported successfully!"))
