import datetime
import json

from flask import Flask, redirect, render_template, request, jsonify
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

@app.route('/phone', methods=['POST'])
def save_phone_num():
    if request.method == 'POST':
        try:
            phone_num = request.json.get('phoneNum', '')
            print('post method success, phoneNum: ' + phone_num)
            _save_phone_num(phone_num)
            return jsonify(success=True)
        except AttributeError:
            print('post method error')
            return 'error'

@app.route('/thanks', methods=['GET'])
def thanks():
    return render_template('thanks.html')

def _save_phone_num(phone_num):
    if db.session.query(Contact).filter_by(phone_num=phone_num).count() > 0:
        pass # already exists
    else:
        new_contact = Contact(phone_num=phone_num)
        db.session.add(new_contact)
        db.session.commit()



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8123)