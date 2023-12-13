
from flask import Flask
from flask import flash
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for


app = Flask(__name__)
    

@app.get('/israel') 
def present():   
    return render_template("index.html")
   
   
if __name__ == '__main__':
    app.run('0.0.0.0', 6060, debug=True)
    

    