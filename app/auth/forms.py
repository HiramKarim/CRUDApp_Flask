from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..modelsobj.Employee import Employee

class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """

    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        EqualTo('confirm_password')
    ])

    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        print(f'field data {field.data}')

        employee_found = Employee.find_by_email(field.data)

        if employee_found:
            raise ValidationError('Email is already in use.')

    # def validate_username(self, field):
    #     if Employee.find_by_email(username=field.data):
    #         raise ValidationError('Username is already in use.')


class LoginForm(FlaskForm):
    """
    Form for users to login
    """

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')