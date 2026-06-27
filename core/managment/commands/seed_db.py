from django.core.management.base import BaseCommand
from core.product_queries import tag_seed, category_seed, product_seed

class Command(BaseCommand):
	help = "Create records for Category, Tag"
	def handle(self, *args, **options):
		self.stdout.write("Start seeding...")
		try:
			tag_seed()
			category_seed()
			product_seed()
			self.stdout.write(self.style.SUCCESS(f"Records successfuly created"))
		except Exception as e:
			self.stdout.write(self.style.ERROR(f"Error seeding: {e}"))
		