from flask import Blueprint, render_template

from .. manage import *

main = Blueprint('main', __name__)

CURRENT_USER = 'aoi_suzuki1'

@main.route('/')
@main.route('/explore-services')
def explore_services():
    global CURRENT_USER

    if user_is_client(CURRENT_USER):
        return render_template(
            'client/explore_services.html',
            services=all_service_posts(),
            featured_service_categories=featured_service_categories(),
            featured_service_providers=featured_service_providers(),
            featured_service_posts=featured_service_posts()
        )
    elif user_is_service_provider(CURRENT_USER):
         return render_template(
            'service_provider/explore_services.html',
            services=all_service_posts(),
            featured_service_categories=featured_service_categories(),
            featured_service_providers=featured_service_providers(),
            featured_service_posts=featured_service_posts()
        )

@main.route('/client')
def landing_page_client():
    return render_template('client/landing_page.html')

@main.route('/service-provider')
def landing_page_service_provider():
    return render_template('service_provider/landing_page.html')