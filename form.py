from flask import Flask, render_template,request
import requests


app = Flask(__name__)


l=[]
@app.route("/",methods=["POST","GET"])
def api():
    if request.form.get("input")!=None:
        val=request.form.get("input")
        url="https://api.mfapi.in/mf/"+val
        resp=requests.get(url)
        temp=resp.json()
        id=temp.get("meta").get("scheme_code")
        fund_house=temp.get("meta").get("fund_house")
        scheme_code=temp.get("data")[0].get("nav")
        dic={"id":id,"fund_house":fund_house,"scheme_code":scheme_code}
        l.append(dic)
        return render_template("index.html",data=l)
    return render_template("index.html")

l=[]
@app.route("/siva",methods=["POST","GET"])
def api1():
    val=request.json.get("input")
    url="https://api.mfapi.in/mf/"+str(val)
    resp=requests.get(url)
    temp=resp.json()
    id=temp.get("meta").get("scheme_code")
    fund_house=temp.get("meta").get("fund_house")
    scheme_code=temp.get("data")[0].get("nav")
    dic={"id":id,"fund_house":fund_house,"scheme_code":scheme_code}
    l.append(dic)
    return l




if __name__=="__main__":
    app.run(debug=True)