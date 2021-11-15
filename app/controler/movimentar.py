from os import error
from app.model.models import Colaborador,Local,Movimentado
from flask import render_template, request, url_for, redirect, flash
from app import db
from app.controler.allData import Total
import app.controler.APIexternas as API


class MovimentarControler():
    def movimentarlista():

        select = '''SELECT * FROM patrimonio p WHERE p.id_patrimonio NOT IN (SELECT m.id_patrimonio FROM movimentado m);'''
        
        

        todasPatrimonio = db.session.execute(select)

        todasColaborador = Colaborador.query.all()
        #todasPatrimonio = Patrimonio.query.all()
        todasMovimentado = Movimentado.query.all()



        for a in todasColaborador: 
        
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',a ,type(todasPatrimonio))

      
        

    
        if request.method == 'POST':
            id_patrimonio_mov = request.form['id_patrimonio_mov']
            id_colaborador_mov = request.form['id_colaborador_mov']
            print(id_colaborador_mov,id_patrimonio_mov)

            dadosMovimentar = Movimentado(id_patrimonio_mov,id_colaborador_mov)

            db.session.add(dadosMovimentar)
            db.session.commit()
            flash(f"O Patrimonio foi vinculado com sucesso!")
            return redirect(url_for("movimentar"))

        return render_template("movimentar.html",todasColaborador=todasColaborador,
                                            todasPatrimonio=todasPatrimonio,
                                            todasMovimentado = todasMovimentado,
                                            data=Total.total())
        

    def movimentarEdita():

        if request.method == "POST":
            idUpdate = Local.query.get(request.form.get("id"))
            print(f"valor do id", {request.form.get("id")})

            print(idUpdate)
            idUpdate.nome = request.form["nome"]
            idUpdate.cidade = request.form["cidade"]

            db.session.commit()

            flash(f"O {request.form['nome'].upper()}, foi atualizado com sucesso.")

            return redirect(url_for("local"))

    def movimentarApaga(id):

        idDelete = Movimentado.query.get(id)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>',idDelete)
        db.session.delete(idDelete)
        db.session.commit()
        flash(f"ID {id}, foi apagado com sucesso.")
        return redirect(url_for("movimentar"))
