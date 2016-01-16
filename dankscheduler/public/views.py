# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from dankscheduler.extensions import login_manager
from dankscheduler.public.forms import LoginForm
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
