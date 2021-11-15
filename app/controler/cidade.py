from os import error
from app.model.models import Cidade
from flask import render_template, request, url_for, redirect, flash
from app import db
from app.controler.allData import Total
import app.controler.APIexternas as API


class CidadeControler:
    def cidadelista():

        todosCidades = Cidade.query.all()

        if request.method == "POST":

            nome = request.form["nome"]
            estado = request.form["estado"]
            pais = request.form["pais"]


            dadosCidade = Cidade(nome, estado, pais)

            db.session.add(dadosCidade)

            print(nome, estado, pais)

            try:
                db.session.commit()

                flash(f"{nome.upper()}, foi cadastrado com sucesso.")

                return redirect(url_for("cidade"))

            except error:
                print(
                    error,
                    "Entrei aqui>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",
                )
                flash(f"{request.form['nome'].upper()}, Ação inválida!!!.")
                return render_template("cidade.html", todosCidades=todosCidades)

        return render_template("cidade.html", todosCidades=todosCidades, estados = API.IBGE.estadoBrasil(),paises = API.IBGE.pais(),data=Total.total())

    def cidadeEdita():
        
        if request.method == "POST":
            idUpdate = Cidade.query.get(request.form.get("id"))
            print(f"valor do id", {request.form.get("id")})

            print(idUpdate)
            idUpdate.nome = request.form["nome"]
            idUpdate.estado = request.form["estado"]
            idUpdate.pais = request.form["pais"]

            db.session.commit()

            flash(f"{request.form['nome'].upper()}, foi atualizado com sucesso.")

            return redirect(url_for("cidade"))

    def cidadeApaga(id):
        idDelete = Cidade.query.get(id)
        print(idDelete)
        db.session.delete(idDelete)
        db.session.commit()
        flash(f"ID {id}, foi apagado com sucesso")
        return redirect(url_for("cidade"))