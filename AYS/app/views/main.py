from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def main_content():
    return render_template('terms_and_conditions.html')