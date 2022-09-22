from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.workout import Workout
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():

    if not User.validate_register(request.form):
        return render_template('index.html', user=request.form)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id

    return redirect('/dashboard')


@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)

    if not user:
        flash("Invalid Email", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password", "login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    return render_template("dashboard.html", user=User.get_one_with_workouts(data))


@app.route('/all/workouts')
def allWorkouts():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    return render_template("allworkouts.html", user=User.get_by_id, workouts=Workout.get_all())


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
