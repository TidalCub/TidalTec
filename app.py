from flask import Flask, request, render_template, redirect
from sqlalchemy import false
from dbmodule import Wholesale, session 
import jsonhandelermodule as js
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/wholesale")
def wholesale():
    data = session.query(Wholesale).all()
    return render_template('wholesale.html',data = data)

@app.route("/wholesale/<catagory>")
def catagory(catagory):
    data = session.query(Wholesale).filter_by(Cat = catagory).all()
    catinfo = js.wholesale(catagory,False)
    print(catinfo)
    return render_template('catogorypage.html',data = data, Cat=catinfo["title"],)

@app.route("/wholesale/<catagory>/<product>")
def wholeproduct(catagory,product):
    print(product)
    info = js.wholesale(product,True)
    
    colours = info["colour"].split(",")
    return render_template('productpage.html', title=product,img1 = info["Img1"],desc=info["Desc"],colour = colours, price=info["Price"])

@app.route("/accessories")
def accessories():
   
   return render_template('accessories.html')

@app.route("/accessories/M4BBFunnel")
def M4BBfunnel():
    colours = ["black","grey","red","white","yellow","green"]
    return render_template('/producttemp/m4Funnel.html', colour = colours)

@app.route("/accessories/mp5Funnel")
def Mp5funnel():
    colours = ["black","grey","red","white","yellow","green"]
    return render_template('/producttemp/mp5Funnel.html', colour = colours)

@app.route("/accessories/AUGFunnel")
def AUGfunnel():
    colours = ["black","grey","red","white","yellow","green"]
    return render_template('/producttemp/AUGFunnel.html', colour = colours)



@app.route("/accessories/MOSFunnel")
def MOSfunnel():
    colours = ["black","grey","red","white","yellow","green"]
    return render_template('/producttemp/MOSFunnel.html', colour = colours)
    
@app.route("/accessories/AKFunnel")
def AKfunnel():
    colours = ["black","grey","red","white","yellow","green"]
    return render_template('/producttemp/AKFunnel.html', colour = colours)
if __name__ == "__main__":
    app.run(debug=True)


