from flask import render_template, request
from . import api


@api.route('/', methods=['GET'])
def get_home():
    return render_template('home.html')