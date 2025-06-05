from flask import Blueprint, render_template
import pandas as pd

main = Blueprint('main', __name__)

@main.route('/')
def index():
    data = pd.read_csv('data/sample_crime_data.csv')
    return render_template('index.html', crime_count=len(data))
