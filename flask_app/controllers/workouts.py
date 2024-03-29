from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.workout import Workout
from flask_app.models.user import User


@app.route('/new/workout')
def new_workout():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    return render_template('new_workout.html', user=User.get_by_id(data))


@app.route('/create/workout', methods=['POST'])
def create_workout():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Workout.validate_workout(request.form):
        return redirect('/new/workout')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "compound_lift": request.form["compound_lift"],
        "compound_lift2": request.form["compound_lift2"],
        "compound_lift3": request.form["compound_lift3"],
        "accessory": request.form["accessory"],
        "accessory2": request.form["accessory2"],
        "accessory3": request.form["accessory3"],

        "user_id": session["user_id"]
    }
    Workout.save(data)
    return redirect('/dashboard')


@app.route('/edit/workout/<int:id>')
def edit_workout(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("edit_workout.html", edit=Workout.get_one(data), user=User.get_by_id(user_data))


@app.route('/update/workout', methods=['POST'])
def update_workout():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Workout.validate_workout(request.form):
        return redirect('/update/workout')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "compound_lift": request.form["compound_lift"],
        "compound_lift2": request.form["compound_lift2"],
        "compound_lift3": request.form["compound_lift3"],
        "accessory": request.form["accessory"],
        "accessory2": request.form["accessory2"],
        "accessory3": request.form["accessory3"],
        "id": request.form["id"]
    }
    Workout.update(data)
    return redirect('/dashboard')


@app.route('/workout/<int:id>')
def show_workout(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("show_workout.html", workout=Workout.get_one(data), user=User.get_by_id(user_data))


@app.route('/destroy/workout/<int:id>')
def destroy_workout(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    Workout.destroy(data)
    return redirect('/dashboard')
