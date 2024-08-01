from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:XXXXXX@localhost:5432/traveldb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(200), nullable=False)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/destinations')
def destinations():
    destinations = Destination.query.all()
    return render_template('destinations.html', destinations=destinations)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/add_destination', methods=['GET', 'POST'])
def add_destination():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        image = request.form['image']
        new_destination = Destination(name=name, description=description, image=image)
        try:
            db.session.add(new_destination)
            db.session.commit()
            return redirect('/destinations')
        except:
            return 'There was an issue adding your destination'
    else:
        return render_template('add_destination.html')

@app.route('/edit_destination/<int:id>', methods=['GET', 'POST'])
def edit_destination(id):
    destination = Destination.query.get_or_404(id)
    if request.method == 'POST':
        destination.name = request.form['name']
        destination.description = request.form['description']
        destination.image = request.form['image']
        try:
            db.session.commit()
            return redirect('/destinations')
        except:
            return 'There was an issue updating your destination'
    else:
        return render_template('edit_destination.html', destination=destination)

@app.route('/delete_destination/<int:id>')
def delete_destination(id):
    destination = Destination.query.get_or_404(id)
    try:
        db.session.delete(destination)
        db.session.commit()
        return redirect('/destinations')
    except:
        return 'There was an issue deleting your destination'

if __name__ == '__main__':
    app.run(debug=True)
