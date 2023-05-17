from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from faker import Faker
from course.models import Student
from urllib.request import urlopen


class Command(BaseCommand):
    help = 'Generates fake data and saves it to the database'

    def add_arguments(self, parser):
        parser.add_argument('num_records', type=int, help='Number of fake records to create')

    def handle(self, *args, **options):
        fake = Faker()
        num_records = options['num_records']

        for _ in range(num_records):
            my_model = Student(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                phone=fake.phone_number(),
                address=fake.street_address(),
                city=fake.city(),
                state=fake.state(),
                zip_code=fake.zipcode(),
                date_of_birth=fake.date_of_birth(),
                gender=fake.random_element(elements=('M', 'F')),
                nationality=fake.country()
            )

            # Download a sample image from the internet
            img_url = 'https://picsum.photos/200/300'  # Change to your desired image URL
            img_name = img_url.split('/')[-1]
            img_content = urlopen(img_url).read()
            img_file = ContentFile(img_content, name=img_name)
            my_model.image.save(img_name, img_file, save=True)
            my_model.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {num_records} fake data records'))
