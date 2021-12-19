from flask import Blueprint, render_template, redirect

from .. manage import *

main = Blueprint('main', __name__)

session = {'username' : 'aoi_suzuki2'}

@main.route('/')
@main.route('/test')
def test():
    user = session['username']
    return f"{user}: {get_user_password(user)}"

@main.route('/explore-services')
def explore_services():
    
    user = session['username']

    if user is None:
        return redirect('/sign-in')
    elif user_is_client(user):
        return render_template(
            'client/explore_services.html',
            services=all_service_posts(),
            featured_service_categories=featured_service_categories(),
            featured_service_providers=featured_service_providers(),
            featured_service_posts=featured_service_posts()
        )
    elif user_is_service_provider(user):
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