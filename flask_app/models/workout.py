from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Workout:
    db = 'gains'

    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.description = db_data['description']
        self.compound_lift = db_data['compound_lift']
        self.compound_lift2 = db_data['compound_lift2']
        self.compound_lift3 = db_data['compound_lift3']
        self.accessory = db_data['accessory']
        self.accessory2 = db_data['accessory2']
        self.accessory3 = db_data['accessory3']

        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls, data):
        query = """INSERT INTO workouts (name, description, compound_lift, compound_lift2, compound_lift3,accessory, accessory2, accessory3, user_id) 
        VALUES (%(name)s,%(description)s,%(compound_lift)s,%(compound_lift2)s,%(compound_lift3)s,%(accessory)s,%(accessory2)s,%(accessory3)s,%(user_id)s);"""
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM workouts;"
        results = connectToMySQL(cls.db).query_db(query)
        Workouts = []
        for row in results:
            print(row['name'])
            Workouts.append(cls(row))
        return Workouts

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM workouts WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])
# UDPATE

    @classmethod
    def update(cls, data):
        query = """UPDATE workouts SET name=%(name)s, description=%(description)s, compound_lift=%(compound_lift)s,compound_lift2=%(compound_lift2)s,compound_lift3=%(compound_lift3)s, accessory=%(accessory)s, 
        accessory2=%(accessory2)s, accessory3=%(accessory3)s, updated_at=NOW() WHERE id = %(id)s;"""
        return connectToMySQL(cls.db).query_db(query, data)
# DESTROY

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM workouts WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
# VALIDATE

    @staticmethod
    def validate_workout(workout):
        is_valid = True
        if len(workout['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters", "workout")
        if len(workout['compound_lift']) < 3:
            is_valid = False
            flash("Compound Lift must be at least 3 characters", "workout")
        if len(workout['accessory']) < 3:
            is_valid = False
            flash("Accessory must be at least 3 characters", "workout")

        return is_valid
