from flask import Flask,render_template,redirect,flash,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from functools import wraps



app=Flask(__name__)

@app.route("/")
def Anasayfa():
    return render_template("islemsayfa.html")

@app.route("/filmler")
def film():
    return render_template("film.html")
@app.route("/hikayeler")
def hikayeler():
    return render_template("hikayeler.html")

@app.route("/hikayeler/keloglan")
def keloglan():
    return render_template("/hikayeler/keloglan.html")

@app.route("/hikayeler/dürümcekli")
def dürümcekli():
    return render_template("hikayeler/dürümcekli.html")
@app.route("/hikayeler/akilli")
def akilli():
    return render_template("/hikayeler/akillikiz.html" )

@app.route("/siirler")
def siir():
    return render_template("siir.html")

@app.route("/siirler/orhanveli")
def Orhan():
    return render_template("includes/orhanveli.html")

@app.route("/siirler/behcet")
def Behcet():
    return render_template("includes/behcet.html")

@app.route("/behcet/gece-ve-yas")
def gece():
    return render_template("siirler/gece.html")

@app.route("/behcet/nilüfer")
def nilüfer():
    return render_template("siirler/nilüfer.html")

@app.route("/behcet/sayet-ask")
def ask():
    return render_template("siirler/sayet.html")

@app.route("/behcet/solgun")
def solgun():
    return render_template("siirler/solgun.html")

@app.route("/behcet/dönmedolap")
def donmedolap():
    return render_template("siirler/donmedolap.html")


@app.route("/orhan/istanbul")
def istanbul():
    return render_template("/siirler/istanbul.html")

@app.route("/orhan/bayrak")
def bayrak():
    return render_template("/siirler/bayrak.html")

@app.route("/orhan/mahvetti")
def mahvetti():
    return render_template("/siirler/mahvetti.html")
@app.route("/orhan/bayram")
def bayram():
    return render_template("/siirler/bayram.html")
@app.route("/siirler/canyücel")
@app.route("/orhan/genclik")
def genclik():
    return render_template("/siirler/genclik.html")

@app.route("/orhan/bedava")
def bedava():
    return render_template("/siirler/bedava.html")

def Can():
    return render_template("includes/canyücel.html")

@app.route("/canyücel/sende_gizle")
def sende_gizle():
    return render_template("siirler/sende_gizle.html")

 
@app.route("/canyücel/eger")
def eger():
    return render_template("siirler/eger.html")

@app.route("/canyücel/sevgiduvarı")
def sevgi():
    return render_template("siirler/sevgiduvarı.html")
@app.route("/canyücel/hayattaencok")
def encok():
    return render_template("siirler/hayattaencok.html")

@app.route("/canyücel/degisik")
def degisik():
    return render_template("siirler/degisik.html")
@app.route("/canyücel/agaclarıkesmeyin")
def agaclar():
    return render_template("siirler/agaclarıkesmeyin.html")

@app.route("/siirler/nazım")
def nazim():
    return render_template("includes/nazim.html")

@app.route("/nazim/cevizagacı")
def cevizagaci():
    return render_template("siirler/cevizagacı.html")

@app.route("/nazim/benseno")
def benseno():
    return render_template("siirler/benseno.html")

@app.route("/nazim/dostluk")
def dostluk():
    return render_template("siirler/dostluk.html")
@app.route("/nazim/maviliman")
def maviliman():
    return render_template("siirler/maviliman.html")

@app.route("/nazim/bessatırla")
def bessatırla():
    return render_template("siirler/bessatırla.html")

if __name__=="__main__":
    app.run(debug=True)
