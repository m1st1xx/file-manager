from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
import sqlite3
import os

from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from urllib.parse import unquote
from urllib.parse import quote
from pathlib import Path

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'  # для сессий

UPLOAD_BASE = "uploads"
SUBJECTS = ["ПОКС","ОППиФКС","ЭОСИ","АСОС","ОАКС","ИКГ","МПС"]

def init_db():
    conn=sqlite3.connect("users.db")
    c=conn.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 first_name TEXT NOT NULL,
                 last_name TEXT NOT NULL,
                 group_number TEXT NOT NULL,
                 password_hash TEXT NOT NULL,
                 folder_path TEXT NOT NULL)''')

    conn.commit()
    conn.close()

def create_user_folders(first_name,last_name):
    folder_path=f"{first_name}_{last_name}"
    user_path=os.path.join(UPLOAD_BASE,folder_path)
    Path(user_path).mkdir(parents=True,exist_ok=True)
    for subject in SUBJECTS:
        Path(os.path.join(user_path,subject)).mkdir(parents=True, exist_ok=True)
    return user_path


def get_user_folder():
    if 'first_name' not in session or 'last_name' not in session:
        return None
    return os.path.join(UPLOAD_BASE, f"{session['first_name']}_{session['last_name']}")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['POST'])
def register():
    first_name=request.form['first_name']
    last_name = request.form['last_name']
    group_number= request.form['group_number']
    password = request.form['password']
    password_hash= generate_password_hash(password)
    folder_path= create_user_folders(first_name,last_name)


    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('''INSERT INTO users (first_name,last_name,group_number,password_hash,folder_path)
        VALUES (?,?,?,?,?)''',(first_name,last_name,group_number,password_hash,folder_path))
         
        conn.commit()
        conn.close()
        flash("Аккаунт создан! Теперь войдите.", "success")
        return redirect(url_for('index'))
    except sqlite3.IntegrityError:
        flash("Пользователь с таким именем и фамилией уже существует.", "error")
        return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    group_number = request.form['group_number']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''SELECT password_hash FROM users 
                 WHERE first_name = ? AND last_name = ? AND group_number = ?''',
              (first_name, last_name, group_number))
    user = c.fetchone()
    conn.close()

    if user and check_password_hash(user[0], password):
        session['user'] = f"{first_name} {last_name}"
        session['first_name'] = first_name
        session['last_name'] = last_name
        return redirect(url_for('main'))
    else:
        flash("Неверные данные", "error")
        return redirect(url_for('index'))

@app.route('/main')
def main():
    if 'user' not in session:
        flash("Сначала войдите!", "error")
        return redirect(url_for('index'))
    return render_template('main.html')


@app.route('/download')
def download_select():
    if 'user' not in session:
        return redirect(url_for('index'))
    return render_template('select_subject.html', mode='download')


@app.route('/upload')
def upload_select():
    if 'user' not in session:
        return redirect(url_for('index'))
    return render_template('select_subject.html', mode='upload')



@app.route('/<mode>/<subject>', methods=['GET','POST'])
def subject_files(subject,mode):
    if mode not in ['download','upload']:
        return 'НЕВЕРНЫЙ РЕЖИМ', 400
    if subject not in SUBJECTS:
        return "НЕПРАВИЛЬНЫЙ ПРЕДМЕТ", 400
    user_folder= get_user_folder()
    if not user_folder:
        return redirect(url_for('index'))
    subject_path=os.path.join(user_folder,subject)
    if request.method == 'POST' and mode == 'upload':
        if 'file' not in request.files:
            flash('ФАЙЛ НЕ ВЫБРАН','error')
            return redirect(request.url)
        file=request.files['file']
        if file.filename == '':
            flash('ФАЙЛ НЕ ВЫБРАН', 'error')
            return redirect(request.url)
        if file:
            filepath= os.path.join(subject_path,file.filename)
            file.save(filepath)
            flash("ФАЙЛ УСПЕШНО ЗАГРУЖЕН",'success')
            return redirect(request.url)
    files=[]
    if os.path.exists(subject_path):
        files = [f for f in os.listdir(subject_path) if os.path.isfile(os.path.join(subject_path,f))]
    return render_template('subject_files.html', mode=mode, subject=subject, files=files)

@app.route('/delete_file<subject>/<filename>', methods=['POST'])
def delete_file(subject,filename):
    if subject not in SUBJECTS:
        return "INCORRECT SUBJECT", 400
    if 'user' not in session:
        return redirect(url_for('index'))
    decoded_filename = unquote(filename)
    user_folder= get_user_folder()
    if not user_folder:
        return redirect(url_for('index'))
    file_path= os.path.join(user_folder,subject,decoded_filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
        flash(f"Файл '{decoded_filename}' удалён.","success")
    else:
        flash("Файл не найден.","error")
    return redirect(url_for('subject_files', mode='upload',subject=subject))




@app.route('/download_file/<subject>/<filename>')
def download_file(subject,filename):
    if subject not in SUBJECTS:
        return "INCORRECT SUBJECT", 400
    user_folder=get_user_folder()
    if not user_folder:
        return redirect(url_for('index'))
    subject_path=os.path.join(user_folder,subject)
    return send_from_directory(subject_path,filename,as_attachment=True)

@app.route('/reset_password',methods=['GET','POST'])
def reset_password():
    if request.method=='POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        group_number = request.form['group_number']
        new_password = request.form['new_password']
        conn= sqlite3.connect('users.db')
        c=conn.cursor()
        c.execute('''SELECT id FROM users 
        WHERE first_name=? AND last_name = ? AND group_number = ? '''
                  ,(first_name,last_name,group_number))
        user=c.fetchone()
        if user:
            password_hash=generate_password_hash(new_password)
            c.execute(''' UPDATE users SET password_hash = ?
            WHERE id = ?''',(password_hash,user[0]))
            conn.commit()
            flash("Пароль успешно изменён!","success")
        else:
            flash("Пользователь не найден.","error")
        conn.close()
        return redirect(url_for('index'))
    return render_template('reset_password.html')




@app.context_processor
def inject_subjects():
    return dict(SUBJECTS=SUBJECTS)




@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
