from flask import Flask,render_template,request,redirect,flash
from models import *
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """render home page with available pets"""
    pets = Pet.query.all()
    return render_template('home.html', pets = pets)

@app.route('/pets/<int:petid>')
def view_pet(petid):
    """render detail pet page with btn to edit individual pet"""
    pet = Pet.query.get_or_404(petid)
    return render_template('pet_detail.html', pet = pet)

@app.route('/pets/new', methods = ["GET","POST"])
def add_pets():
    """pet add form, handle adding"""
    form = AddPetForm()
    if(form.validate_on_submit()):
        name = form.name.data
        age = form.age.data
        photo_url = form.photo_url.data
        species = form.species.data
        available = True if form.available.data==1 else False
        note = form.note.data
        new_pet = Pet(name = name, age = age, photo_url = photo_url, species = species, available= available, notes= note)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"Added {name} to our pet list",'info')
        return redirect(f'/pets/{new_pet.id}')
    else:
        return render_template("pet_add_form.html",form = form)

@app.route('/pets/<int:petid>/edit', methods = ["GET","POST"])
def edit_pets(petid):
    """pet edit form, handle editing"""
    pet = Pet.query.get_or_404(petid)
    form = AddPetForm(obj=pet)
    if(form.validate_on_submit()):
        pet.name = form.name.data
        pet.age = form.age.data
        pet.photo_url = form.photo_url.data
        pet.species = form.species.data
        pet.available = True if form.available.data==1 else False
        pet.note = form.note.data
        db.session.add(pet)
        db.session.commit()
        flash(f"Change information of {form.name.data} to our pet list",'info')
        return redirect(f'/pets/{pet.id}')
    else:
        return render_template("pet_edit_form.html",form = form)
