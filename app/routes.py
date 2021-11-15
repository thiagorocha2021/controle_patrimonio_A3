from app import app, login_manager, db
from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, logout_user, login_required
from app.model.models import User,Test
from app.controler.fornecedor import *
from app.controler.cargo import *
from app.controler.filial import *
from app.controler.cidade import *
from app.controler.colaborador import *
from app.controler.patrimonio import *
from app.controler.local import *
from app.controler.movimentar import *


#Test.test(False)
#Test.test(True)



##LOGIN##
@app.route("/", methods=["GET", "POST"])
def login():
   

 
    if request.method == "POST":
        email = request.form.get("email")
        pwd = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            print("####################senha errada")
            return render_template("login.html", erro=True)

        login_user(user)
        # return render_template("home.html")
        return redirect(url_for("patrimonio"))

    return render_template("login.html")


###LOGOFF##
@app.route("/logout/", methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for("login"))


###HOME###
@app.route("/home/", methods=["GET", "POST"])
@login_required
def home():
    return render_template("home.html",qtdadeColaborador = Total.total())


###REGISTRA###
@app.route("/register/", methods=["GET", "POST"])
@login_required
def register():

    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        pwd = request.form.get("password")

        print(nome, email, pwd)

        if nome and email and pwd:
            user = User(nome, email, pwd)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("login"))

    return render_template("register.html")


############CARGO################
@app.route("/cargo/", methods=["GET", "POST"])
@login_required
def cargo():
    return CargoControler.cargolista()


@app.route("/cargoUpdate/", methods=["GET", "POST"])
@login_required
def cargoUpdate():
    return CargoControler.cargoEdita()


@app.route("/cargoDelete/<id>/", methods=["GET", "POST"])
@login_required
def cargoDelete(id):
    return CargoControler.cargoApaga(id)


############FILIAL################
@app.route("/filial/", methods=["GET", "POST"])
@login_required
def filial():
    return FilialControler.filiallista()


@app.route("/filialUpdate/", methods=["GET", "POST"])
@login_required
def filialUpdate():
    return FilialControler.filialEdita()


@app.route("/filialDelete/<id>/", methods=["GET", "POST"])
@login_required
def filialDelete(id):
    return FilialControler.filialApaga(id)


############CIDADE################
@app.route("/cidade/", methods=["GET", "POST"])
@login_required
def cidade():
    return CidadeControler.cidadelista()


@app.route("/cidadeUpdate/", methods=["GET", "POST"])
@login_required
def cidadeUpdate():
    return CidadeControler.cidadeEdita()


@app.route("/cidadeDelete/<id>/", methods=["GET", "POST"])
@login_required
def cidadeDelete(id):
    return CidadeControler.cidadeApaga(id)


############COLABORADOR################
@app.route("/colaborador/", methods=["GET", "POST"])
@login_required
def colaborador():
    return ColaboradorControler.colaboradorlista()


@app.route("/colaboradorUpdate/", methods=["GET", "POST"])
@login_required
def colaboradorUpdate():
    return ColaboradorControler.colaboradorEdita()


@app.route("/colaboradorDelete/<id>/", methods=["GET", "POST"])
@login_required
def colaboradorDelete(id):
    return ColaboradorControler.colaboradorApaga(id)


############FORNECEDOR################
@app.route("/fornecedor/", methods=["GET", "POST"])
@login_required
def fornecedor():
    return FornecedorControler.fornecedorlista()


@app.route("/fornecedorUpdate/", methods=["GET", "POST"])
@login_required
def fornecedorUpdate():
    return FornecedorControler.fornecedorEdita()


@app.route("/fornecedorDelete/<id>/", methods=["GET", "POST"])
@login_required
def fornecedorDelete(id):
    return FornecedorControler.fornecedorApaga(id)


############PATRIMONIO################


@app.route("/patrimonio/", methods=["GET", "POST"])
@login_required
def patrimonio():
    return PatrimonioControler.patrimoniolista()


@app.route("/patrimonioUpdate/", methods=["GET", "POST"])
@login_required
def patrimonioUpdate():
    return PatrimonioControler.patrimonioEdita()


@app.route("/patrimonioDelete/<id>/", methods=["GET", "POST"])
@login_required
def patrimonioDelete(id):
    return PatrimonioControler.patrimonioApaga(id)


####################LOCAL######################



@app.route("/local/", methods=["GET", "POST"])
@login_required
def local():
    return LocalControler.locallista()


@app.route("/localUpdate/", methods=["GET", "POST"])
@login_required
def localUpdate():
    return LocalControler.localEdita()


@app.route("/localDelete/<id>/", methods=["GET", "POST"])
@login_required
def localDelete(id):
    return LocalControler.localApaga(id)


####################MOVIMENTAR######################


@app.route("/movimentar/",methods=["GET","POST"])
@login_required
def movimentar():

    return MovimentarControler.movimentarlista()
    

@app.route("/movimentadoDelete/<id>/", methods=["GET", "POST"])
@login_required
def movimentadoDelete(id):
    return MovimentarControler.movimentarApaga(id)
