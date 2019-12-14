import datetime

from flask import Flask, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from database import Contact


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts-collection.db'
db = SQLAlchemy(app)


@app.route('/')
def redirect_to_application():
    def check_date(dt, year, month, day):
        if dt.year == year and dt.month == month and dt.day == day:
            return True
        return False
    today = datetime.datetime.today()
    print(today)
    if check_date(today, 2019, 12, 16):
        return redirect('https://forms.gle/CCWrpZYGfp88EcKJ8')
    else:
        return render_template('not_yet.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8123)