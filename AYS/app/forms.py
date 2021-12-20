from flask import Markup
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SelectField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Regexp, NumberRange
from extensions import db
from .manage import *

class SignInForm(FlaskForm):
    user_id = StringField(
        label=("Username"),
        validators=[
            DataRequired(),        
        ],
        render_kw={'type': 'text'}
    )

    user_password = StringField(
        label=("Password"),
        validators=[
            DataRequired(),
        ],
        render_kw={'type': 'password'}
    )

    submit = SubmitField(label=('Submit'))

    def validate_user_id(form, field):
        if not user_id_exists(field.data):
            raise ValidationError("The username you entered does not exist.")
    
    def validate_user_password(form, field):
        user = form.user_id.data
        if user_id_exists(user):
            if field.data != get_user_password(form.user_id.data):
                raise ValidationError("The password you entered is incorrect.")