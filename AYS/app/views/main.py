from flask import Blueprint, render_template

from .. manage import *

main = Blueprint('main', __name__)

@main.route('/')
def main_content():
    return render_template(
        'explore_services.html',
        services=all_services(),
        featured_service_categories=featured_service_categories(),
        featured_service_providers=featured_service_providers()
    )