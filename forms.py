from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,SelectField, RadioField,TextAreaField
from wtforms.validators import InputRequired, Optional,URL

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name",validators=[InputRequired()])
    age = IntegerField("Pet Age",validators=[Optional()])
    photo_url = StringField("Pet Photo",validators=[Optional(),URL()],default = 'https://images.unsplash.com/photo-1558824575-76e80bd6d090?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60')
    species = SelectField('Species', choices=[('cat', 'cat'), ('dog', 'dog'),('porcupine','porcupine')])
    available = RadioField('Available', choices= [(1, 'Yes'),(0, 'No')], default = True,coerce=int)
    note = TextAreaField('note',validators=[Optional()])