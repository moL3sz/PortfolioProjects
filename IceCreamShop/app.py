from flask import Flask,request,render_template
from sqlalchemy import SQLAlchemy
app = Flask(__name__,static_folder='/static')








@app.route("/")
def index():
    return "Hello world"
if __name__ == "__main__":
    app.run(port=8080,debug=True)


