"""Seed file to make sample data for users db."""

from models import connect_db, db,Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
dog1= Pet(name = 'Chuck',
    species= 'dog',
    photo_url = 'https://images.unsplash.com/photo-1534361960057-19889db9621e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60',
    age = 2,
    notes = 'This is a stupid dog',
    available = True)
dog2 = Pet(name = 'Brown',
    species= 'dog',
    photo_url = 'https://images.unsplash.com/photo-1518020382113-a7e8fc38eac9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60',
    age = 1.5,
    notes = 'This is a cute dog',
    available = True)
dog3 = Pet(name = 'Zoe',
    species= 'dog',
    photo_url = 'https://images.unsplash.com/photo-1537151608828-ea2b11777ee8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60',
    age = 1,
    notes = 'This is a beautiful dog',
    available = True)
cat1 = Pet(name='Randy', species= 'cat', 
            photo_url = 'https://images.unsplash.com/photo-1494256997604-768d1f608cac?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60',
            age= 1)
cat2 = Pet(name='Bob', species= 'cat', 
            photo_url = 'https://images.unsplash.com/photo-1548247416-ec66f4900b2e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60',
            age= 2)
cat3 = Pet(name='Sushi', species= 'cat', 
            age= 3)


# Add new objects to session, so they'll persist
db.session.add(dog1)
db.session.add(dog2)
db.session.add(dog3)

db.session.add(cat1)
db.session.add(cat2)
db.session.add(cat3)

# Commit--otherwise, this never gets saved!
db.session.commit()

