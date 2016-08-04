from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('index.html')
    
    
@main.route('/queues')

def queues():
    return render_template('queues.html')
