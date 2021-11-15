from os import error
from app.model.models import Colaborador,Local,Filial
from flask import render_template, request, url_for, redirect, flash
from app import db
from app.controler.allData import Total
import app.controler.APIexternas as API

class LocalControler():
    def locallista():
        todosLocal = Local.query.all()
        todosColaborador = Colaborador.query.all()
        todasFilial = Filial.query.all()

        if request.method == "POST":
            nome = request.form["nome"]
            id_colaborador = request.form["id_colaborador"]

            dados = Local(nome,id_colaborador)

            db.session.add(dados)
            db.session.commit()

            flash(f"Local {nome.upper()}, foi cadastrado com sucesso!")

            return redirect(url_for("local"))

        
        return render_template("local.html", todosLocal=todosLocal,
                                            todosColaborador=todosColaborador,
                                            todasFilial=todasFilial,
                                            data=Total.total())

    def localEdita():

        if request.method == "POST":
            idUpdate = Local.query.get(request.form.get("id"))
            print(f"valor do id>>>>>>>>>>>>>>>>>>>>>>>>>>>>", {request.form.get("id")})

            #print(idUpdate)
            idUpdate.nome = request.form["nome"]
            idUpdate.id_colaborador = request.form["id_colaborador"]

            db.session.commit()

            flash(f"O {request.form['nome'].upper()}, foi atualizado com sucesso.")

            return redirect(url_for("local"))

    def localApaga(id):

        idDelete = Local.query.get(id)
        print(idDelete)
        db.session.delete(idDelete)
        db.session.commit()
        flash(f"ID {id}, foi apagado com sucesso.")
        return redirect(url_for("local"))


