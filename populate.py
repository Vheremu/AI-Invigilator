import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myproject.settings')
import django
django.setup()
import random
from groups.models import Group
from faker import Faker
fakegen = Faker()
def populate(N=20):
    for entry in range(N):
        fake_name = fakegen.job()
        fake_description = fakegen.text()
        grp = Group.objects.get_or_create(name=fake_name,description=fake_description)[0]
if __name__=='__main__':
    print('population script is running' )
    populate(20)
    print('population complete')
