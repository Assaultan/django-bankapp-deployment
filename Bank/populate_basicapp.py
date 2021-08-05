import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Bank.settings')

import django
django.setup()

###Script
import random
from basicapp.models import Customers
from faker import Faker

fake = Faker()

l=[]
for i in range(20):
    l.append(random.randint(10000,40000))
tup=tuple(l)

def populate(N=5):
    for i in range(N):

        #create fake email,name,balance
        fake_name = fake.name()
        fake_email = fake.email()

        Cust = Customers.objects.get_or_create(name=fake_name,email=fake_email,balance=tup[i])[0]

if __name__=='__main__':
    print("Start")
    populate(10)
    print("Complete")
