from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    department = db.Column(db.String)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    course_number = db.Column(db.String)

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    department = db.Column(db.String)
    department_code = db.Column(db.String)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    professor_id = db.Column(db.Integer)
    course_id = db.Column(db.Integer, index=True)
    rating = db.Column(db.Integer)
    review = db.Column(db.String)
    __table_args__ = (db.Index('idx_rating_profid_rating', "professor_id", "rating"), )

with app.app_context():
    db.create_all()

@app.route("/", methods=['GET'])
def index():
    return redirect(url_for('get_professors'))


@app.route('/professors', methods=['GET'])
def get_professors():
    professors = Professor.query.all()
    departments = Department.query.all()
    return render_template('professors.html', professors=professors, departments=departments)
    

@app.route('/addProfessor', methods=['GET', 'POST'])  
def add_professor():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname') 
        department = request.form.get('department')
        prof = Professor(firstname=firstname, lastname=lastname, department=department)
        db.session.add(prof)
        db.session.commit()
        request.method = 'GET'
        return redirect(url_for('get_professors'))

@app.route('/infoProf/<id>', methods=['GET'])
def info_prof(id):
    prof = Professor.query.filter_by(id=id).first()
    rats = db.session.execute(
        text('''
            SELECT review, rating, course_number FROM rating 
            INNER JOIN course ON rating.course_id = course.id
            WHERE professor_id = :prof_id;
            '''
        ), 
        {"prof_id": id})
    stats = {
        "avgrating": avg_prof_rating(id), 
        "numcourses": totalcourses(id),
        "numratings": totalratings(id)
    }
    return render_template("professorinfo.html", professor=prof, ratings = rats, stats=stats)

@app.route('/searchcourse', methods=['POST'])
def search_course():
    course = request.form.get('course')
    courses = db.session.execute(text('SELECT * FROM course WHERE course_number LIKE :c;'), {'c': f"%{course}%"})
    return render_template("courselist.html", courses=courses)

@app.route('/addrating', methods=['POST'])
def add_rating():
    if request.method == "POST":
        review = request.form.get("review")
        rating = request.form.get("rating")
        course_id = request.form.get("course_number")
        professor_id = request.form.get("professor_id")

        rat = Rating(review=review, rating=rating, course_id=course_id, professor_id=professor_id)
        db.session.add(rat)
        db.session.commit()
        request.method = 'GET'
        return redirect(f"infoProf/{professor_id}")

def avg_prof_rating(prof_id):
    rating = db.session.execute(
        text('''
            SELECT avg(rating) FROM rating 
            WHERE professor_id = :prof_id;
            '''),
        {"prof_id": prof_id}).fetchone()
    return round(rating[0],2) if rating[0] != None else rating[0]

def totalratings(prof_id):
    rating = db.session.execute(
        text('''
            SELECT count(rating) FROM rating 
            WHERE professor_id = :prof_id;
            '''),
        {"prof_id": prof_id}).fetchone()
    return rating[0]

def totalcourses(prof_id):
    rating = db.session.execute(
        text('''
            SELECT count(distinct course_id) FROM rating 
            WHERE professor_id = :prof_id;
            '''),
        {"prof_id": prof_id}).fetchone()
    return rating[0]

if __name__ == "__main__":
    app.run()