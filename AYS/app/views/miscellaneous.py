from flask import Blueprint, render_template

from .. manage import *

miscellaneous = Blueprint('miscellaneous', __name__, url_prefix='/miscellaneous')

@miscellaneous.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')

@miscellaneous.route('/terms_and_conditions')
def terms_and_conditions():
    return render_template('terms_and_conditions.html')