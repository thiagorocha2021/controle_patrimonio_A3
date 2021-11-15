from app.model.models import Filial, Cidade
from flask import render_template, request, url_for, redirect, flash
from app import db
from app.controler.allData import Total

class FilialControler:
    def filiallista():

        todasFilial = Filial.query.all()
        todasCidade = Cidade.query.all()

        for a in todasFilial:
            print(a.cidade.nome)

        if request.method == "POST":
            nome = request.form["nome"]
            endereco = request.form["endereco"]
            cnpj = request.form["cnpj"]
            id_cidade = request.form["id_cidade"]

            dadosFilial = Filial(nome, endereco, cnpj, id_cidade)
            db.session.add(dadosFilial)
            try:
                db.session.commit()
                flash(f"{nome.upper()}, foi cadastrado com sucesso. {nome}")

                return redirect(url_for("filial"))

            except:
                print(
                    "Entrei aqui>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
                )
                flash(f"{request.form['nome'].upper()}, Ação inválida!!!.")
                return render_template(
                    "filial.html", todasFilial=todasFilial, todasCidade=todasCidade
                )

        return render_template(
            "filial.html", todasFilial=todasFilial, todasCidade=todasCidade,data=Total.total())

    def filialEdita():
        if request.method == "POST":
            idUpdate = Filial.query.get(request.form.get("id"))
            print(f"valor do id", {request.form.get("id")})

            print(idUpdate)
            idUpdate.nome = request.form["nome"]
            idUpdate.endereco = request.form["endereco"]
            idUpdate.cnpj = request.form["cnpj"]
            idUpdate.id_cidade = request.form["id_cidade"]

            db.session.commit()

            flash(f"{request.form['nome'].upper()}, foi atualizado com sucesso.")

            return redirect(url_for("filial"))

