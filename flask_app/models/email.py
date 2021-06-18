from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['emails']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO emails (emails, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        return connectToMySQL('email_validation').query_db( query, data )

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('email_validation').query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email))
        return emails

    @staticmethod
    def validate_email(data):
        is_valid = True
        
        if not email_regex.match(data['email']): 
            flash("Email is not valid!")
            is_valid = False
        return is_valid 

    
