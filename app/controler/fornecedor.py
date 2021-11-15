from os import error
from app.model.models import Fornecedor
from flask import render_template, request, url_for, redirect, flash
from app import db
from app.controler.allData import Total






class FornecedorControler:
    def fornecedorlista():

        todosFornecedor = Fornecedor.query.all()

        if request.method == "POST":
            nome = request.form["nome"]
            cnpj = request.form["cnpj"]
            endereco = request.form["endereco"]
            telefone = request.form["telefone"]
            cidade = request.form["cidade"]
            pais = request.form["pais"]

            dados = Fornecedor(nome, cnpj, endereco, telefone, cidade, pais)

            db.session.add(dados)
            db.session.commit()

            flash(f"Fornecedor {nome.upper()} cadastrado com sucesso!")

            return redirect(url_for("fornecedor"))

        return render_template("fornecedor.html", todosFornecedor=todosFornecedor,data=Total.total())

    def fornecedorEdita():
        if request.method == "POST":
            idUpdate = Fornecedor.query.get(request.form.get("id"))
            print(f"valor do id", {request.form.get("id")})

            print(idUpdate)
            idUpdate.nome = request.form["nome"]
            idUpdate.cnpj = request.form["cnpj"]
            idUpdate.endereco = request.form["endereco"]
            idUpdate.telefone = request.form["telefone"]
            idUpdate.cidade = request.form["cidade"]
            idUpdate.pais = request.form["pais"]

            db.session.commit()

            flash(f"O {request.form['nome'].upper()}, foi atualizado com sucesso.")

            return redirect(url_for("fornecedor"))

    def fornecedorApaga(id):
        idDelete = Fornecedor.query.get(id)
        print(idDelete)
        db.session.delete(idDelete)
        db.session.commit()
        flash(f"ID {id}, foi apagado com sucesso.")
        return redirect(url_for("fornecedor"))

