from flask import Flask, render_template, request, url_for, flash, redirect
import os, datetime
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import abort

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app = Flask('__name__')
app.config['SECRET_KEY'] = 'your secret key'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

class Posts(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
   title = db.Column(db.String(80), nullable=False)
   email = db.Column(db.String(80), nullable=False)
   telefone = db.Column(db.String(80), nullable=False)
   sexo = db.Column(db.String(10), nullable=False)
   servico = db.Column(db.String(20), nullable=False)
   data = db.Column(db.String(20), nullable=False)
   horario = db.Column(db.String(20), nullable=False)
   content = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    posts = Posts.query.all()
    return render_template('index.html', posts=posts)

def get_post(post_id):
   post = Posts.query.filter_by(id=post_id).first()
   if post is None:
      abort(404)
   return post

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/sobre')
def sobre():
        return render_template('sobre.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        email = request.form['email']
        telefone = request.form['telefone']
        sexo = request.form['sexo']
        servico = request.form['servico']
        data = request.form['data']
        horario = request.form['horario']
        content = request.form['content']

        if not title:
            flash('O título é obrigatório!')
        else:
            post = Posts(title=title, email=email, telefone=telefone, sexo=sexo, servico=servico, data=data, horario=horario, content=content)
            db.session.add(post)
            db.session.commit()
            db.session.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        email = request.form['email']
        telefone = request.form['telefone']
        sexo = request.form['sexo']
        servico = request.form['servico']
        data = request.form['data']
        horario = request.form['horario']
        content = request.form['content']

        if not title:
            flash('Título é obrigatório!')
        else:
            post.title = title
            post.email = email
            post.telefone = telefone
            post.sexo = sexo
            post.servico = servico
            post.data = data
            post.horario = horario
            post.content = content
            db.session.commit()
            db.session.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    db.session.delete(post)
    db.session.commit()
    db.session.close()
    return redirect(url_for('index'))