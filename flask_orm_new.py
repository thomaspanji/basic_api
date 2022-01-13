from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)


class User(db.Model):

   __tablename__ = 'users'

   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(255), unique=True, nullable=False)
   email = db.Column(db.String(255), unique=True, nullable=False)
   dob = db.Column(db.Date, nullable=False)
   age = db.Column(db.Integer, nullable=False)

   def __init__(self, name, email, dob):
      self.name = name
      self.email = email
      self.dob = self.to_date(dob)
      self.age = self.calculate_age(self.dob)

   @staticmethod
   def to_date(dob):
      return date.fromisoformat(dob)
   
   @staticmethod
   def calculate_age(dob):
         today = date.today()
         return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))


@app.route('/')
def users():
   return render_template('users.html', users = User.query.all() )


@app.route('/register', methods = ['GET', 'POST'])
def register():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['email'] or not request.form['dob']:
         flash('Please enter all the fields', 'error')
      else:         
         user = User(
            name=request.form['name'],
            email=request.form['email'],
            dob=request.form['dob']
         )
         
         db.session.add(user)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('users'))

   return render_template('register.html')


if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)