import random
from flask import Flask, redirect, render_template, request, session
from datetime import datetime

app=Flask(__name__)
app.secret_key="clave secreta"


@app.route("/",methods=['GET'])
def index():
    if "total" not in session:
        session["total"] = 0
    print("renderizando tempalte")
    return render_template("index.html")
    
@app.route("/process-money",methods=['POST'])
def process_money():       
    print(request.form["stage"])
    if request.form["stage"]=="farm":
        session["random"] = random.randint(10,20)
        session["total"] += session["random"]
        session["date"] = datetime.now()
        session["random_casino"] = 1
        
    elif request.form["stage"]=="cave":
        session["random"] = random.randint(5,10)
        session["total"] += session["random"]
        session["date"] = datetime.now()
        session["random_casino"] = 1
    
    elif request.form["stage"]=="house":
        session["random"] = random.randint(2,5)
        session["total"] += session["random"]
        session["date"] = datetime.now()
        session["random_casino"] = 1
    
    elif request.form["stage"]=="casino":
        session["random_casino"]=random.randint(1,2)
        session["random"] = random.randint(0,50)
        if (session["random_casino"] == 1):
            session["total"] += session["random"]
        else:
            session["total"] -= session["random"]
        session["date"] = datetime.now()

    dict_append = {
        "random_number":session["random"],
        "random_casino":session["random_casino"],
        "stage":request.form["stage"],
        "date_time":session["date"]
        
    }
    if "dict_append" not in session:
        session["dict_append"]=[]
    session["dict_append"].append(dict_append)
    print(session["dict_append"])
    return redirect("/")

@app.route("/clear",methods=['GET'])
def clear(): 
    session.clear()
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)