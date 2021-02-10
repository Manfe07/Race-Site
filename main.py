from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
import db_handler

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

class CreateTeam(FlaskForm):
    name = StringField('Name')
    name_short = StringField('Kurzform')
    info = TextAreaField('Info')
    submit = SubmitField('Create')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getRaces')
def get_races():
    return db_handler.getRaces()

@app.route('/createTeam', methods=['GET', 'POST'])
def createRace():
    form = CreateTeam()
    if form.validate_on_submit():
        db_handler.addTeam(form.name.data ,form.name_short.data, form.info.data)
        return redirect("/createTeam")
    return render_template('createRace.html', title='Create Race', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=1337)