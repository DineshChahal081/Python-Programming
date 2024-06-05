from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

#MY db connection
local_server=True
app = Flask(__name__)
app.secret_key='berlinchaudhary'

#app.config['SQLALCHEMY_DATABASE_URL']='mysql://username:password@localhost/database_table_name'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/hms' 
db=SQLAlchemy(app)  

#here we will create db models that is tables
class Test(db.Model):
      id=db.Column(db.Integer,primary_key=True)
      name=db.Column(db.String(100))
      email=db.Column(db.String(100))


@app.route('/')
def hello_world():
    a=Test.query.all()
    print()
    return render_template('index.html')
      #return render_template('index.html')
    '''try:
        Test.query.all()
        return 'My databse is connected'
    except:
        return 'My database is not connected' '''

'''@app.route('/test')
def test():
    return render_template('test.html')'''
  

'''@app.route('/')
def hello_world():
    return 'Hello, BERLIN'

@app.route('/test')
def test():
    return 'This is for testing purpose'

@app.route('/home')
def home():
    return "This is my home page" '''

if __name__ == "__main__":
   app.run(debug=True)
