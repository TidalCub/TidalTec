from flask import Flask, render_template_string, request, render_template, redirect,session
from sqlalchemy import false
from dbmodule import Wholesale, sesh 
import jsonhandelermodule as js
from modules import formatedlist
import json
app = Flask(__name__)

with open('./jsonfiles/config.json') as config_file:
    config = json.load(config_file)

app.secret_key = config.get("Secret_Key")

@app.before_request
def make_session_permanent():
    session.permanent = True

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/wholesale")
def wholesale():
    data = sesh.query(Wholesale).all()
    return render_template('blockpage.html')

@app.route("/wholesale/<catagory>")
def catagory(catagory):
    data = sesh.query(Wholesale).filter_by(Cat = catagory).all()
    catinfo = js.wholesale(catagory,False)
    
    return render_template('catogorypage.html',data = data, Cat=catinfo["title"],)

@app.route("/wholesale/<catagory>/<product>")
def wholeproduct(catagory,product):
    
    info = js.wholesale(product,True)
    
    colours = info["colour"].split(",")
    return render_template('productpage.html', title=product,img1 = info["Img1"],desc=info["Desc"],colour = colours, price=info["Price"])

@app.route("/accessories")
def accessories():
   
   return render_template('accessories.html')

@app.route("/accessories/M4BBFunnel", methods=["GET","POST"])
def M4BBfunnel():
    colours = ["black","grey","red","white","yellow","green","blue"]
    
    if request.method == "POST":
        item = ("img ","M4 BB Funnel" , request.form['colours'] , 1, "5.48")
        if 'cart' in session:
            
            session['cart'] = session.get('cart') + item # reading and updating session data
        else:
            session['cart'] = item
    return render_template('/producttemp/m4Funnel.html', colour = colours)

@app.route("/accessories/mp5Funnel",methods=["GET","POST"])
def Mp5funnel():
    colours = ["black","grey","red","white","yellow","green"]
    

    return render_template('/producttemp/mp5Funnel.html', colour = colours)

@app.route("/accessories/AUGFunnel",methods=["GET","POST"])
def AUGfunnel():
    colours = ["black","grey","red","white","yellow","green"]
    if request.method == "POST":
        item = ("img ","AUG BB Funnel" , request.form['colours'] , 1, "5.48")
        if 'cart' in session:
            
            session['cart'] = session.get('cart') + item # reading and updating session data
        else:
            session['cart'] = item

    return render_template('/producttemp/AUGFunnel.html', colour = colours)



@app.route("/accessories/MOSFunnel",methods=["GET","POST"])
def MOSfunnel():
    colours = ["black","grey","red","white","yellow","green","blue"]
    if request.method == "POST":
        item = ("img ","MOSCART BB Funnel" , request.form['colours'] , 1, "5.48")
        if 'cart' in session:
            
            session['cart'] = session.get('cart') + item # reading and updating session data
        else:
            session['cart'] = item

    return render_template('/producttemp/MOSFunnel.html', colour = colours)

@app.route("/accessories/AKFunnel",methods=["GET","POST"])
def AKfunnel():
    colours = ["black","grey","red","white","yellow","green"]
    return render_template('/producttemp/AKFunnel.html', colour = colours)


@app.route("/basket")
def basket():
    
    cart = session.get('cart')
    
    if cart != None:

        formadlist = formatedlist(cart)
        total = 0
        for i in range(len(formadlist)):
            
            total += float(formadlist[i][5])
    else:
        formadlist = None
    
    items = {}
    items = {
        "name":"M4BBFunnel",
        
        "description":"Green",
        "unit_ammount":{"currency_code": "GBP","value": "5.48"},
        "quantity": "2",
    }

        

    
    
    return render_template('basket.html',cart = formadlist,total = total, item = items)

@app.route("/pop")
def pop():
    session.pop('cart')
    return redirect ("/basket", code=302)

@app.route("/basket/<id>/")
def remove(id):
    cart = session.get('cart')
    cart = list(cart)
    for i in range(0,5):
        cart.pop(int(id)*5)
    
    cart = tuple(cart)
    session['cart'] = cart
    return redirect ("/basket", code=302)

if __name__ == "__main__":
    app.run(debug=True)


