# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for

from dankscheduler.public.forms import ContactForm
from dankscheduler.utils import flash_errors
blueprint = Blueprint('public', __name__, static_folder='../static')


@blueprint.route('/')
def home():
    """Home page."""
    return render_template('public/home.html')


@blueprint.route('/about/')
def about():
    """About page."""
    return render_template('public/about.html')


@blueprint.route('/contact/', methods=['GET', 'POST'])
def contact():
    """Contact page."""
    form = ContactForm()
    
    if request.method == 'POST':
        return 'Form posted.'
        
    elif request.method == 'GET':
        return render_template('public/contact.html', form=form)