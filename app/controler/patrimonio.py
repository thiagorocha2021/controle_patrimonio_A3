from os import error
from app.model.models import Fornecedor,Patrimonio
from flask import render_template, request, url_for, redirect, flash
from app import db
from app.controler.allData import Total
import app.controler.APIexternas as API
from app.controler.calculeValueImpostos import *




class PatrimonioControler:
    def patrimoniolista():
        todosPatrimonio = Patrimonio.query.all()
        todosFornecedor = Fornecedor.query.all()

        if request.method == "POST":
            nome = request.form["nome"]
            categoria = request.form["categoria"]
            n_serie = request.form["n_serie"]
            n_patrimonio = request.form["n_patrimonio"]
            id_fornecedor = request.form["fornecedor"]
            print(id_fornecedor, ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            dadosPatrimonio = Patrimonio(
                nome, categoria, n_serie, n_patrimonio, id_fornecedor
            )

            db.session.add(dadosPatrimonio)
            db.session.commit()

            flash(
                f"{nome.upper()}, foi cadastrado com sucesso no número de patrimônio: {n_patrimonio}"
            )

            return redirect(url_for("patrimonio"))

        return render_template(
            "patrimonio.html",
            todosPatrimonio=todosPatrimonio,
            todosFornecedor=todosFornecedor, 
            categorias = API.MercadoLivre.cotegorias(),
            data=Total.total()
        )

    def patrimonioEdita():
        if request.method == "POST":
            idUpdate = Patrimonio.query.get(request.form.get("id"))
            print(f"valor do id", {request.form.get("id")})

            print(idUpdate)
            idUpdate.nome = request.form["nome"]
            idUpdate.categoria = request.form["categoria"]
            idUpdate.n_serie = request.form["n_serie"]
            idUpdate.n_patrimonio = request.form["n_patrimonio"]
            idUpdate.fornecedor_id = request.form["id_fornecedor"]

            db.session.commit()

            flash(
                f"{request.form['nome'].upper()}, foi atualizado com sucesso no número de patrimônio: {request.form['n_patrimonio']}"
            )

            return redirect(url_for("patrimonio"))

    def patrimonioApaga(id):
        idDelete = Patrimonio.query.get(id)
        print(idDelete)
        db.session.delete(idDelete)
        db.session.commit()
        flash(f"ID {id}, foi apagado com sucesso")
        return redirect(url_for("patrimonio"))

    def CalculaValorPatrimonio(valor,frete,ICMS,IPI):

        #100,10,False,5

        ValueICMS = valor_icms(valor,ICMS) #M 3
        valueIPI = valor_ipi(valor,IPI) #5
        valueFrete = valor_frete(valor, frete) #110
    

        return valueFrete + valueIPI + ValueICMS




