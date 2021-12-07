from flask import Blueprint, render_template
import pymysql

from extensions import db

main = Blueprint('main', __name__)

def all_services():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""
        SELECT Service.service_title, Service.service_description, Service.service_user_id, Service.service_user_rating, Service.service_user_level, Service.service_user_is_trusted, Service.service_date_posted, Service.service_schedule, Service.service_location, ServiceType.service_type_name AS service_type, ServiceCategory.service_category_name AS service_category, Service.service_amount
        FROM `Service`
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