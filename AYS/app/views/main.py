from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def main_content():
    return render_template('landing_page_service_provider.html')