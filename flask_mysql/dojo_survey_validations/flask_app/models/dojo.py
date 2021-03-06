from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = 'dojo_survey_schema'

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s)"
        result = connectToMySQL(db).query_db(query, data)
        return result

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            flash("*Name must be at least 3 characters long.")
            is_valid = False
        if len(dojo['location']) < 3:
            flash("*Location must be at least 3 characters long.")
            is_valid = False
        if len(dojo['language']) < 1:
            flash("*Language must be at least 1 character long.")
            is_valid = False
        return is_valid

