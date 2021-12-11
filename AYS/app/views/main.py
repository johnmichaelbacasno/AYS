from flask import Blueprint, render_template

from .. manage import *

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/explore_services')
def explore_services():
    return render_template(
        'explore_services.html',
        services=all_service_posts(),
        featured_service_categories=featured_service_categories(),
        featured_service_providers=featured_service_providers(),
        featured_service_posts=featured_service_posts()
    )

@main.route('/landing_page_service_provider')
def landing_page_service_provider():
    return render_template('landing_page_service_provider.html')

@main.route('/landing_page_client')
def landing_page_client():
    return render_template('landing_page_client.html')