from flask import Blueprint, render_template
import pymysql

from extensions import db

main = Blueprint('main', __name__)

def all_services():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""
        SELECT Service.service_title, Service.service_description, User.user_name AS service_user, User.user_rating AS service_user_rating, User.user_level as service_user_level, User.user_is_trusted AS service_user_is_trusted, Service.service_date_posted, Service.service_schedule, Service.service_location, ServiceType.service_type_name AS service_type, ServiceCategory.service_category_name AS service_category, Service.service_amount
        FROM `Service`
        JOIN `User` ON Service.service_user = User.user_id
        JOIN `ServiceType` ON Service.service_type = ServiceType.service_type_id
        JOIN `ServiceCategory` ON ServiceType.service_category = ServiceCategory.service_category_id
    """)
    services = cursor.fetchall()
    cursor.close()
    conn.close()
    return services

@main.route('/')
def main_content():
    return render_template('explore_services.html', services=all_services())