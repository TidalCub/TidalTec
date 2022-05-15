from flask import Flask, request, render_template, redirect


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/wholesale")
def wholesale():
    return render_template('wholesale.html')
if __name__ == "__main__":
    app.run(debug=True)

