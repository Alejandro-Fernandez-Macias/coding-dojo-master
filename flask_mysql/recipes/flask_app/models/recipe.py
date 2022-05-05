from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from ..models.user import User

db = 'recipes'

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.under30 = data['under30']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes ( name, under30, description, instructions, date_made, user_id ) VALUES ( %(name)s, %(under30)s, %(description)s,%(instructions)s, %(date_made)s, %(user_id)s );"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = f"UPDATE recipes SET name = %(name)s, %(under30)s, %(description)s, %(instructions)s %(date_made)s WHERE id = %(id)s ;"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(db).query_db(query)
        all_recipes = []
        for row in results:
            print(row['date_made'])
            all_recipes.append(cls(row))
        return all_recipes

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM  recipes WHERE id = %(id)s"
        result = connectToMySQL(db).query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_alll_created_recipes(cls):
        query = "SELECT * FROM  users LEFT JOIN recipes ON recipes.user_id = users.id"
        results = connectToMySQL(db).query_db(query)
        print(results)
        pass

    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("*Name must be at least 3 characters long", "recipe")
            is_valid = False
        if len(data['description']) < 3:
            flash("*Description must be at least 3 characters long", "recipe")
            is_valid = False
        if len(data['instructions']) < 3:
            flash("*Instructions must be at least 3 characters long", "recipe")
            is_valid = False
        if data['date_made'] == "":
            is_valid = False
            flash("*No date entered , please input date", "recipe")
        return is_valid



