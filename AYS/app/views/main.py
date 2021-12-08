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

@main.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')

@main.route('/terms_and_conditions')
def terms_and_conditions():
    return render_template('terms_and_conditions.html')