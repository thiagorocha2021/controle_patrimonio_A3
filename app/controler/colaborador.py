from os import error
from app.model.models import Colaborador, Filial, Cargo
from flask import render_template, request, url_for, redirect, flash
from app import db
from app.controler.allData import Total


class ColaboradorControler:
    def colaboradorlista():

        todasColaborador = Colaborador.query.all()
        todasFilial = Filial.query.all()
        todosCargo = Cargo.query.all()

        if request.method == "POST":

            nome = request.form["nome"]
            email = request.form["email"]
            telefone = request.form["telefone"]
            endereco = request.form["endereco"]
            id_filial = request.form["id_filial"]
            id_cargo = request.form["id_cargo"]

            print(nome, email, telefone, endereco, id_filial, id_cargo)

            dadosColaborador = Colaborador(
                nome, email, telefone, endereco, id_filial, id_cargo,
            )

            db.session.add(dadosColaborador)

            try:
                db.session.commit()

                flash(f"{nome.upper()}, foi cadastrado com sucesso.")

                return redirect(url_for("colaborador"))

            except error:
                flash(f"{request.form['nome'].upper()}, Ação inválida!!!.")
                return render_template(
                    "colaborador.html",
                    todasColaborador=todasColaborador,
                    todasFilial=todasFilial,
                    todosCargo=todosCargo,
                )

        return render_template(
            "colaborador.html",
            todasColaborador=todasColaborador,
            todasFilial=todasFilial,
            todosCargo=todosCargo,data=Total.total())

    def colaboradorEdita():
        if request.method == "POST":
            idUpdate = Colaborador.query.get(request.form.get("id"))
            print(f"valor do id", {request.form.get("id")})

            print(idUpdate)
            idUpdate.nome = request.form["nome"]
            idUpdate.email = request.form["email"]
            idUpdate.telefone = request.form["telefone"]
            idUpdate.endereco = request.form["endereco"]
            idUpdate.id_filial = request.form["id_filial"]
            idUpdate.id_cargo = request.form["id_cargo"]

            db.session.commit()

            flash(f"{request.form['nome'].upper()}, foi atualizado com sucesso.")

            return redirect(url_for("colaborador"))

    def colaboradorApaga(id):
        idDelete = Colaborador.query.get(id)
        print(idDelete)
        db.session.delete(idDelete)
        db.session.commit()
        flash(f"ID {id}, foi apagado com sucesso")
        return redirect(url_for("colaborador"))

