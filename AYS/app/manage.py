import pymysql

from extensions import db

def all_service_posts():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""
        SELECT ServicePost.service_post_id,
               ServicePost.service_post_title,
               ServicePost.service_post_description,
               User.user_id AS service_post_user_id,
               User.user_first_name AS service_post_user_first_name,
               User.user_middle_name AS service_post_user_middle_name,
               User.user_last_name AS service_post_user_last_name,
               User.user_rating AS service_post_user_rating,
               User.user_level as service_post_user_level,
               User.user_is_trusted AS service_post_user_is_trusted,
               ServicePost.service_post_date_posted,
               ServicePost.service_post_schedule,
               ServicePost.service_post_location,
               ServicePost.service_post_service_type AS service_post_service_type_id,
               ServiceType.service_type_name AS service_post_service_type_name,
               ServiceCategory.service_category_id AS service_post_service_category_id,
               ServiceCategory.service_category_name AS service_post_service_category_name,
               ServicePost.service_post_amount
        FROM `ServicePost`
        JOIN `User` ON ServicePost.service_post_user = User.user_id
        JOIN `ServiceType` ON ServicePost.service_post_service_type = ServiceType.service_type_id
        JOIN `ServiceCategory` ON ServiceType.service_category = ServiceCategory.service_category_id
    """)
    all_service_posts = cursor.fetchall()
    cursor.close()
    conn.close()
    return all_service_posts

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

def featured_service_posts():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""
        SELECT ServicePost.service_post_id,
               ServicePost.service_post_title,
               ServicePost.service_post_description,
               User.user_id AS service_post_user_id,
               User.user_first_name AS service_post_user_first_name,
               User.user_middle_name AS service_post_user_middle_name,
               User.user_last_name AS service_post_user_last_name,
               User.user_rating AS service_post_user_rating,
               User.user_level as service_post_user_level,
               User.user_is_trusted AS service_post_user_is_trusted,
               ServicePost.service_post_date_posted,
               ServicePost.service_post_schedule,
               ServicePost.service_post_location,
               ServicePost.service_post_service_type AS service_post_service_type_id,
               ServiceType.service_type_name AS service_post_service_type_name,
               ServiceCategory.service_category_id AS service_post_service_category_id,
               ServiceCategory.service_category_name AS service_post_service_category_name,
               ServicePost.service_post_amount
        FROM `ServicePost`
        JOIN `User` ON ServicePost.service_post_user = User.user_id
        JOIN `ServiceType` ON ServicePost.service_post_service_type = ServiceType.service_type_id
        JOIN `ServiceCategory` ON ServiceType.service_category = ServiceCategory.service_category_id
        ORDER BY service_post_user_rating DESC
        LIMIT 3;
    """)
    featured_service_posts = cursor.fetchall()
    cursor.close()
    conn.close()
    return featured_service_posts

def featured_service_categories():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""
        SELECT * FROM `ServiceCategory`
        LIMIT 6;
    """)
    featured_service_categories = cursor.fetchall()
    cursor.close()
    conn.close()
    return featured_service_categories

def featured_service_providers():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""
        SELECT * FROM `User` WHERE `user_account_type` = 'SP'
        ORDER BY user_rating DESC
        LIMIT 6;
    """)
    featured_providers = cursor.fetchall()
    cursor.close()
    conn.close()
    return featured_providers