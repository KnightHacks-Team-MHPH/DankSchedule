from flask import Blueprint, flash, redirect, render_template, request, url_for

from dankscheduler.utils import flash_errors

blueprint = Blueprint('public', __name__, static_folder='../static)


@blueprint.route('/')
def index():
    pass
    
    
