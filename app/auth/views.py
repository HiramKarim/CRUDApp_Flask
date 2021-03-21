from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db

from ..modelsobj.Employee import Employee


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """

    form = RegistrationForm()
    if form.validate_on_submit():
        employee = Employee(userid=0,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            email=form.email.data,
                            password=form.password.data,
                            username=form.username.data,
                            isadmin=True,
                            departamentid=1,
                            roleid=1
                    )

        # add employee to the database
        errortype = employee.insert_employee()

        if errortype != 500:
            flash('You have successfully registered! You may now login.')
        else:
            flash('There was an error trying to register the user.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """

    form = LoginForm()

    if form.validate_on_submit():
        # check whether employee exists in the database and whether
        # the password entered matches the password in the database

        row = Employee.find_employee_by_email(form.email.data)

        print(f'employee data {row}')

        if row is None:
            flash("Email or password are incorrect")
            return

        employee = Employee(
            userid=row[0],
            first_name=row[1],
            last_name=row[2],
            email=row[3],
            password=row[4],
            username=row[5],
            isadmin=row[6],
            departamentid=row[7],
            roleid=row[8]
        )

        # employee = Employee.query.filter_by(email=form.email.data).first()

        if employee is not None and employee.verify_password(employee.password, form.password.data):

            login_user(employee)

            # redirect to the dashbaord page after login
            return redirect(url_for('home.dashboard'))

        # when login details are incorrect
        else:
            flash('Invalid email or password')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """

    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))