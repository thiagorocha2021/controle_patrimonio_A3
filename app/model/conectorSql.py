import pymysql as MySQLdb
from datetime import datetime
import time



con178_6 = ''
cursor178_6 = ''


def fechaConexaoCRUD():
    global con178_6
    global cursor178_6 
 
    try:
        cursor178_6.close()
        con178_6.close()
        #print('\nConexao Mysql 178.38.178.6 fechada com sucesso!!!\n')

    except:
        #print('\nFalha em fechar a conexão, do 177.38.178.6')
        pass



def CRUD6(comando_sql,data,tipo):
    global con178_6
    global cursor178_6 
    
    con178_6 = MySQLdb.connect(host="177.38.178.6", user="root", passwd="mncxkj200877", db="patrimonio_a3")
    cursor178_6 = con178_6.cursor()

    if tipo == 'insert':
        
        
        try:

            cursor178_6.execute(comando_sql,data)        
            con178_6.commit()  
            fechaConexaoCRUD()
  

        except cursor178_6.Error as err:
            print("ERRO DE RETORNO MYSQL: {}".format(err))

    elif tipo == 'select':
        try:

            cursor178_6.execute(comando_sql)        
            data = cursor178_6.fetchall()
            fechaConexaoCRUD()
            return data
            
        except cursor178_6.Error as err:
            print("ERRO DE RETORNO MYSQL: {}".format(err))

    elif tipo == 'update':
        try:

            cursor178_6.execute(comando_sql)
            con178_6.commit() 
            fechaConexaoCRUD()
            #print(True)

        except cursor178_6.Error as err:
            print("ERRO DE RETORNO MYSQL: {}".format(err))
            
    else:
        print('Paramentro do CRUB faltando!!!')



