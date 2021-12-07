from flask import Blueprint, render_template
import pymysql

from extensions import db

main = Blueprint('main', __name__)

def all_services():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM `Service`")
    services = cursor.fetchall()
    cursor.close()
    conn.close()
    return services

@main.route('/')
def main_content():
    return render_template('explore_services.html', services=all_services())