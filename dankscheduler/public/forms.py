# -*- coding: utf-8 -*-
"""Public forms."""
from flask_wtf import Form
from wtforms import Form, TextField, TextAreaField, SelectField, SubmitField


class ContactForm(Form):
    """Contact form."""

    firstname = TextField('First Name')
    lastname = TextField('Last Name')
    schoolyear = SelectField('School Year', choices=[('yr_1', 'Freshman'), ('yr_2', 'Sophomore'), ('yr_3', 'Junior'), ('yr_4', 'Senior')])
    email = TextField('Email')
    message = TextAreaField('Message')
    submit = SubmitField('Submit')

    