from sqlalchemy.orm import relationship
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import datetime







@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):

    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(86), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, nome, email, password):
        self.nome = nome
        self.email = email
        self.password = generate_password_hash(password)
    
    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd) 

class Fornecedor(db.Model):
    __tablename__ = 'fornecedor'
    id_fornecedor = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(45))
    endereco = db.Column(db.String(100))
    telefone = db.Column(db.String(45))
    cidade = db.Column(db.String(45))
    pais = db.Column(db.String(45))

   


    def __init__(self, nome, cnpj,endereco,telefone,cidade,pais):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.telefone = telefone
        self.cidade = cidade
        self.pais = pais

class Patrimonio(db.Model):

    __tablename__ = 'patrimonio'
    id_patrimonio = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(86), nullable=False)
    categoria = db.Column(db.String(84), nullable=False)
    n_serie = db.Column(db.String(128))
    n_patrimonio = db.Column(db.String(128), nullable=False, unique=True)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedor.id_fornecedor'))
    fornecedor = db.relationship('Fornecedor')
    


    def __init__(self, nome, categoria, n_serie,n_patrimonio,fornecedor_id):
        self.nome = nome
        self.categoria = categoria
        self.n_serie = n_serie
        self.n_patrimonio = n_patrimonio
        self.fornecedor_id = fornecedor_id


class Cargo(db.Model):
    __tablename__= 'cargo'
    id_cargo = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self,nome):
        self.nome = nome


class Cidade(db.Model):
    __tablename__ = 'cidade'
    id_cidade = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    estado = db.Column(db.String(100), nullable=False)
    pais = db.Column(db.String(100), nullable=False)
    cidade = db.relationship('Filial')

    def __init__(self, nome, estado, pais):
        self.nome = nome
        self.estado = estado
        self.pais = pais
   

class Filial(db.Model):
    __tablename__ = 'filial'
    id_filial = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(100))
    cnpj = db.Column(db.String(100), nullable=False)
    id_cidade =db.Column(db.Integer, db.ForeignKey('cidade.id_cidade'))
    cidade = db.relationship('Cidade')



    def __init__(self, nome, endereco, cnpj,id_cidade):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.id_cidade = id_cidade



class Colaborador(db.Model):

    __tablename__ = 'colaborador'
    id_colaborador = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True)
    telefone = db.Column(db.String(100))
    endereco = db.Column(db.String(100))
    id_filial = db.Column(db.Integer, db.ForeignKey('filial.id_filial'))
    id_cargo = db.Column(db.Integer, db.ForeignKey('cargo.id_cargo'))
    filial = db.relationship('Filial')
    cargo = db.relationship('Cargo')

    def __init__(self, nome, email, telefone,endereco,id_filial,id_cargo):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.id_filial = id_filial
        self.id_cargo = id_cargo


class Local(db.Model):

    __tablename__ = 'local'
    id_local = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    id_colaborador = db.Column(db.Integer, db.ForeignKey('colaborador.id_colaborador'))
    colaborador = db.relationship('Colaborador')


    def __init__(self, nome,id_colaborador):
        self.nome = nome
        self.id_colaborador = id_colaborador

class Movimentado(db.Model):

    __tablename__ = 'movimentado'
    id_movimentado = db.Column(db.Integer, autoincrement=True, primary_key=True)
    data = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    id_patrimonio = db.Column(db.Integer, db.ForeignKey('patrimonio.id_patrimonio'))
    id_colaborador = db.Column(db.Integer, db.ForeignKey('colaborador.id_colaborador'))
    patrimonio = db.relationship('Patrimonio')
    colaborador = db.relationship('Colaborador')

    def __init__(self, id_patrimonio, id_colaborador):
        self.id_patrimonio = id_patrimonio
        self.id_colaborador = id_colaborador



 
class Test():
    def test(a):
        if a:
            db.create_all()
            
            user = User('debug','debug@debug','123')
            db.session.add(user)
            db.session.commit()





    



    
