from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

db = 'email_validation'

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        result = connectToMySQL(db).query_db(query, data)
        return result

    @classmethod
    def get_all(cls):
        flash("The email address you entered is a valid email adress! Thank you !")
        query = "SELECT * FROM emails;"
        results = connectToMySQL(db).query_db(query)
        emails = []
        for e in results:
            emails.append(cls(e))
        return emails

    @classmethod
    def destroy(clas, data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @staticmethod
    def validate_email(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if not EMAIL_REGEX.match(data['email']):
            flash("Email is an invailid adress")
            is_valid = False
        return is_valid