from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_DEBUG'] = os.getenv('FLASK_DEBUG', 'False') == 'True'
app.config['HOST'] = os.getenv('HOST', '0.0.0.0')
app.config['PORT'] = os.getenv('PORT', 5000)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

@app.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/users', methods=['POST'])
def add_user():
    name = request.form.get('name')
    new_user = User(name=name)
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for('home'))

@app.route('/users/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    if request.form.get('_method') == 'delete':
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('home'))
    
    return jsonify(message="Invalid method."), 405

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['FLASK_DEBUG'])
