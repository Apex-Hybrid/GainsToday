from flask import flash
from .workout import Workout
from flask_app.config.mysqlconnection import connectToMySQL
import re  # the regex module
# create a regular expression object that we'll use later
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    db = "gains"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.workouts = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s)"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def get_by_email(cls, email):
        data = {'email': email}
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query, email)
        if results:
            results = cls(results[0])
        return results

    @classmethod
    def get_one_with_workouts(cls, data):
        query = "SELECT * FROM users LEFT JOIN workouts on users.id = workouts.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL('gains').query_db(query, data)
        print(results)
        user = cls(results[0])
        for row in results:
            w = {
                'id': row['workouts.id'],
                'name': row['name'],
                'description': row['description'],
                'compound_lift': row['compound_lift'],
                'compound_lift2': row['compound_lift2'],
                'compound_lift3': row['compound_lift3'],
                'accessory': row['accessory'],
                'accessory2': row['accessory2'],
                'accessory3': row['accessory3'],

                'user_id': row['user_id'],
                'created_at': row['workouts.created_at'],
                'updated_at': row['workouts.updated_at']
            }
            user.workouts.append(Workout(w))
        return user

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])
# VALIDATE USER

    @ staticmethod
    def validate_register(user):
        is_valid = True
        if User.get_by_email(user['email'].lower()):
            flash("Email already taken.", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email!!!", "register")
            is_valid = False
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters", "register")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters", "register")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters", "register")
            is_valid = False
        if user['password'] != user['confirm']:
            flash("Passwords don't match", "register")
        return is_valid
