from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, logout_user, login_manager, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user
from sqlalchemy import text
# MY db connection
local_server = True
app = Flask(__name__)
app.secret_key = 'momo'

#this is for getting unique user access 
login_manager= LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
             
# app.config['SQLALCHEMY_DATABASE_URL']='mysql://username:password@localhost/database_table_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/hms'
db = SQLAlchemy(app)

# here we will create db models that are tables
class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True) 
    password = db.Column(db.String(1000))
    
class Patients(db.Model):
    pid=db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(50)) 
    name=db.Column(db.String(50))
    gender=db.Column(db.String(50))
    slot=db.Column(db.String(50))
    disease=db.Column(db.String(50))
    time=db.Column(db.String(50), nullable=False)
    date=db.Column(db.String(50), nullable=False)
    dept=db.Column(db.String(50)) 
    number=db.Column(db.String(50))
    
    
class Doctors(db.Model):
    did=db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(50)) 
    doctorname = db.Column(db.String(50))
    dept=db.Column(db.String(100))
        

  
        

# here we will pass endpoints and run the functions


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/doctor', methods=['POST','GET'])
def doctors():
    
    if request.method == "POST":
        
        email = request.form.get('email')
        doctorname = request.form.get('doctorname')
        dept = request.form.get('dept')
        

        query = text("INSERT INTO doctors (email, doctorname, dept) "
                     "VALUES (:email, :doctorname, :dept)")
        
        db.session.execute(query, {
            'email': email,
            'doctorname': doctorname,
            'dept': dept
            
        })
        db.session.commit()
        flash("Information is stored.", "primary")

    return render_template('doctor.html')



from sqlalchemy import text
from flask import request, flash, render_template
from flask_login import login_required

import logging
@app.route('/patients', methods=['POST', 'GET'])
@login_required
def patients():
    doct = db.session.execute(text("SELECT * FROM doctors"))
    for d in doct:
        app.logger.info(f"Doctor: {d.did}, {d.doctorname}, {d.dept}")

    if request.method == "POST":
        email = request.form.get('email')
        name = request.form.get('name')
        gender = request.form.get('gender')
        slot = request.form.get('slot')
        disease = request.form.get('disease')
        time = request.form.get('time')
        date = request.form.get('date')
        dept = request.form.get('dept')
        number = request.form.get('number')

        query = text("INSERT INTO patients (email, name, gender, slot, disease, time, date, dept, number) "
                     "VALUES (:email, :name, :gender, :slot, :disease, :time, :date, :dept, :number)")

        db.session.execute(query, {
            'email': email,
            'name': name,
            'gender': gender,
            'slot': slot,
            'disease': disease,
            'time': time,
            'date': date,
            'dept': dept,
            'number': number
        })
        db.session.commit()
        flash("Booking Confirmed", "info")

    return render_template('patients.html', doct=doct)

@app.route('/bookings')
@login_required
def bookings():
    em = current_user.email

    # Create the parameterized query
    query = text("SELECT * FROM patients WHERE email=:email")

    # Execute the query with the provided parameter
    result = db.session.execute(query, {"email": em})

    # Convert the query result to a list
    query_result = list(result)

    return render_template('bookings.html', query=query_result)


@app.route("/edit/<string:pid>", methods=['POST', 'GET'])
@login_required
def edit(pid):
    posts = Patients.query.filter_by(pid=pid).first()
    if request.method == "POST":
        # Handle form submission and update the patient's information
        email = request.form.get('email')
        name = request.form.get('name')
        gender = request.form.get('gender')
        slot = request.form.get('slot')
        disease = request.form.get('disease')
        time = request.form.get('time')
        date = request.form.get('date')
        dept = request.form.get('dept')
        number = request.form.get('number')
        
        sql = text("UPDATE patients SET email=:email, name=:name, gender=:gender, slot=:slot, disease=:disease, time=:time, date=:date, dept=:dept, number=:number WHERE pid=:pid")
        db.session.execute(sql, {"email": email, "name": name, "gender": gender, "slot": slot, "disease": disease, "time": time, "date": date, "dept": dept, "number": number, "pid": pid})
        db.session.commit()
        
        flash("Slot is Updated", "success")
        return redirect('/bookings')
    
    return render_template('edit.html', posts=posts)



@app.route("/delete/<string:pid>", methods=['POST', 'GET'])
@login_required
def delete(pid):
    query = text("DELETE FROM patients WHERE pid = :pid")
    db.session.execute(query, {"pid": pid})
    db.session.commit()
    flash("Slot Deleted Successfully", "danger")
    return redirect('/bookings')



@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists.", "warning")  # Add flash message for duplicate email
            return render_template('signup.html')
        encpassword = generate_password_hash(password)
        new_user = User(username=username, email=email, password=encpassword)
        db.session.add(new_user)
        db.session.commit()
        flash("Signup Success Please Login", "success")  # Add flash message for successful signup
        return render_template('login.html')
    return render_template('signup.html')

    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Login Success", "success")  # Add flash message for successful login
            return redirect(url_for('index'))
        else:
            flash("Invalid credentials", "danger")  # Add flash message for invalid credentials
    
    return render_template('login.html')



@app.route('/logout')
@login_required
def logout(): 
    logout_user()
    flash("Logout Successful","warning")
    return redirect(url_for('login'))

@app.route('/test')
def test():
    try:
        Test.query.all()
        return 'My database is connected'
    except:
        return 'My database is not connected'

if __name__ == "__main__":
    app.run(debug=True)
 