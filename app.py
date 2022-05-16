from flask import Flask, request, render_template, redirect
from dbmodule import Wholesale, session 

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/wholesale")
def wholesale():
    data = session.query(Wholesale).all()
    return render_template('wholesale.html',data = data)
if __name__ == "__main__":
    app.run(debug=True)


