from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
'''These lines import the necessary modules from the Flask framework. Flask is used to create the
Flask application, and render_template is used to render HTML templates. Additionally, SQLAlchemy is 
imported to handle the database operations.'''


# My db connection
local_server = True
app = Flask(__name__)
app.secret_key = 'momo'
'''local_server is a variable that determines if the application is running on a local server. 
In this case, it is set to True. app is an instance of the Flask application. __name__ represents
the current module (in this case, the main script), and it is used to initialize the Flask application.
secret_key is set to 'momo', which is used for session encryption and should be kept secret in a production
environment.'''


# app.config['SQLALCHEMY_DATABASE_URL']='mysql://username:password@localhost/database_table_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/hms'
db = SQLAlchemy(app)
'''This line configures the database URI for SQLAlchemy, which specifies the location and credentials 
to connect to the MySQL database. In this case, it uses the user 'berlinchaudhary' with the password
'CH20ce081' to connect to the 'hms' database on the IP address '127.0.0.1' with port '3307'.
db is an instance of the SQLAlchemy object, initialized with the Flask application, I chnaged username to root
with no password and localhost with port '3306' which is a default port.'''

# Here we will create db models (tables)
class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
'''This is the database model class Test, which represents a table in the database. It inherits from
db.Model, which is a base class provided by SQLAlchemy.The class has three columns: id, name,
and email. Each column is defined using the db.Column class, specifying the column type and additional 
properties like primary key.'''    

@app.route('/')
def hello_world():
    #a = Test.query.all()
    #print()
    #return render_template('index.html')
    try:
        Test.query.all()
        return 'My databse is connected'
    except:
        return 'My database is not connected'
'''This is a route decorator that associates the URL endpoint '/' with the hello_world function.
When the user accesses the root URL, the function is triggered.
The function tries to query all the records from the Test table using Test.query.all().
If the query is successful, it returns the string 'My database is connected'.
If an exception occurs during the query, it returns the string 'My database is not connected'.'''    

if __name__ == "__main__":
    app.run(debug=True)
'''This conditional statement checks if the current module is the main script that is being executed.
If it is the main script, the Flask application is run with the app.run() method, which starts the development server.
The debug=True parameter enables debug mode, allowing the server to automatically reload on code 
changes and show detailed error messages.'''