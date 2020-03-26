# connect_db.py
# MG 2020.03.23 Connexion bd

import pymysql
import pymysql.cursors

# MG 2020.03.23 Se connecter à la BD.
class DatabaseTools():
    def __init__(self):
        print("Constructeur classe DatabaseTools ")

    def connect_ma_bd(self):
        self.db = pymysql.connect(host="localhost",
                                user="root",
                                password="root",
                                db="guex_matis_tennis_1d_bd_104_2020",
                                cursorclass=pymysql.cursors.DictCursor)
        print("bd connectée impec !!")
        return self

    # MG 2020.03.23 Petite méthode pour fermer la connection à la BD
    def close_connection (self):
        if self.connect_ma_bd().db:
            print("Dans la méthode close_connection et la BD est FERMEE")
            self.db.close()
        else:
            print("Dans la méthode close_connection et y'a rien a fermer")