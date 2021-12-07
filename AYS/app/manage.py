import pymysql

from extensions import db

def all_services():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""
        SELECT Service.service_title,
               Service.service_description,
               User.user_id AS service_user,
               User.user_first_name AS service_user_first_name,
               User.user_middle_name AS service_user_middle_name,
               User.user_last_name AS service_user_last_name,
               User.user_rating AS service_user_rating,
               User.user_level as service_user_level,
               User.user_is_trusted AS service_user_is_trusted,
               Service.service_date_posted,
               Service.service_schedule,
               Service.service_location,
               ServiceType.service_type_name AS service_type,
               ServiceCategory.service_category_name AS service_category,
               Service.service_amount
        FROM `Service`
        JOIN `User` ON Service.service_user = User.user_id
        JOIN `ServiceType` ON Service.service_type = ServiceType.service_type_id
        JOIN `ServiceCategory` ON ServiceType.service_category = ServiceCategory.service_category_id
    """)
    all_services = cursor.fetchall()
    cursor.close()
    conn.close()
    return all_services

def all_service_categories():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""
        SELECT * FROM `ServiceCategory`;
    """)
    all_service_categories = cursor.fetchall()
    cursor.close()
    conn.close()
    return all_service_categories

def all_service_providers():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""
        SELECT * FROM `User` WHERE `user_account_type` = 'SP';
    """)
    all_service_providers = cursor.fetchall()
    cursor.close()
    conn.close()
    return all_service_providers

def all_clients():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""
        SELECT * FROM `User` WHERE `user_account_type` = 'C';
    """)
    all_clients = cursor.fetchall()
    cursor.close()
    conn.close()
    return all_clients

def featured_services():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""
        SELECT Service.service_title,
               Service.service_description,
               User.user_id AS service_user,
               User.user_first_name AS service_user_first_name,
               User.user_middle_name AS service_user_middle_name,
               User.user_last_name AS service_user_last_name,
               User.user_rating AS service_user_rating,
               User.user_level as service_user_level,
               User.user_is_trusted AS service_user_is_trusted,
               Service.service_date_posted,
               Service.service_schedule,
               Service.service_location,
               ServiceType.service_type_name AS service_type,
               ServiceCategory.service_category_name AS service_category,
               Service.service_amount
        FROM `Service`
        JOIN `User` ON Service.service_user = User.user_id
        JOIN `ServiceType` ON Service.service_type = ServiceType.service_type_id
        JOIN `ServiceCategory` ON ServiceType.service_category = ServiceCategory.service_category_id
    """)
    featured_services = cursor.fetchall()
    cursor.close()
    conn.close()
    return featured_services

def featured_service_categories():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""
        SELECT * FROM `ServiceCategory`;
    """)
    featured_service_categories = cursor.fetchall()
    cursor.close()
    conn.close()
    return featured_service_categories

def featured_service_providers():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""
        SELECT * FROM `User` WHERE `user_account_type` = 'SP';
    """)
    featured_providers = cursor.fetchall()
    cursor.close()
    conn.close()
    return featured_providers