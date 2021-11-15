from app.model.models import Cargo
from flask import render_template, request, url_for, redirect, flash
from app import db
from app.controler.allData import Total




class CargoControler:
    def cargolista():

        todosCargos = Cargo.query.all()

        if request.method == "POST":
            nome = request.form["nome"]

            dadosCargo = Cargo(nome)

            db.session.add(dadosCargo)
            try:
                db.session.commit()

                flash(f"{nome.upper()}, foi cadastrado com sucesso. {nome}")

                return redirect(url_for("cargo"))

            except:
                print(
                    "Entrei aqui>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
                )
                flash(f"{request.form['nome'].upper()}, Ação inválida!!!.")
                return render_template("cargo.html", todosCargos=todosCargos)

        return render_template("cargo.html", todosCargos=todosCargos,data=Total.total())

    def cargoEdita():
        if request.method == "POST":
            idUpdate = Cargo.query.get(request.form.get("id"))
            print(f"valor do id", {request.form.get("id")})

            print(idUpdate)
            idUpdate.nome = request.form["nome"]

            db.session.commit()

            flash(f"{request.form['nome'].upper()}, foi atualizado com sucesso.")

            return redirect(url_for("cargo"))

    def cargoApaga(id):
        idDelete = Cargo.query.get(id)
        print(idDelete)
        db.session.delete(idDelete)
        db.session.commit()
        flash(f"ID {id}, foi apagado com sucesso")
        return redirect(url_for("cargo"))



