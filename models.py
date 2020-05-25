"""Models for Adopt."""
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Class to refer to pets"""

    __tablename__ = "pets"
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.Text, nullable = False)
    species= db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text, default= 'https://images.unsplash.com/photo-1558824575-76e80bd6d090?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60')
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable = False, default = True)

    def __repr__(self):
        """representation of the instance when called"""
        return f"<Pet id={self.id} name={self.name} species={self.species} available = {self.available}>"
    

