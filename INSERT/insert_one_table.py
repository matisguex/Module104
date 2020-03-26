# insert_one_table.py
# MG 2020.03.23 le but est d'insérer des valeurs en MySql dans une seule table

import connect_db


class DbInsertOneTable():

    # Constructeur, à chaque instanciation de cette classe "DbInsertOneTable()" les lignes de code de la méthode "__init__ (self)" sont interprétées.
    def __init__ (self):  # Constructeur
        # MG 2020.03.23 CONNECTION A LA BD
        self.connection_dbc = connect_db.DatabaseTools().connect_ma_bd()
        # Ouvre un curseur, c'est indispensable pour se déplacer dans les champs de la BD.
        self.DBcursor = self.connection_dbc.db.cursor()
        print("Constructeur CLASSE DbInsertOneTable")


    def insert_one_record_one_table(self, requete_insert_mysql, valeurs_a_inserer):
        try:
            # MG 2020.03.23 Execute la requête avec un passage de paramètres
            self.DBcursor.execute(requete_insert_mysql, {'values_insert' : valeurs_a_inserer})
            # MG 2020.03.23 L'instruction suivante est indispensable pour confirmer l'insertion des données (en cas de problèmes : rollback)
            self.connection_dbc.db.commit()
            self.DBcursor.close()
        except pymysql.Error as error:
            # MG 2020.03.23 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une ERREUR : %s", error)
            print("connection_dbc.db.rollback() insertOneRecord")
        except pymysql.DataError as error1:
            # MG 2020.03.23 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une DataError : %s", error1)
            print("connection_dbc.db.rollback() insertOneRecord")
        except pymysql.DatabaseError as error2:
            # MG 2020.03.23 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une DatabaseError : %s", error2)
            print("connection_dbc.db.rollback() insertOneRecord")
        except pymysql.Warning as error3:
            # MG 2020.03.23 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une Warning : %s", error3)
            print("connection_dbc.db.rollback() insertOneRecord")
        except pymysql.MySQLError as error4:
            # MG 2020.03.23 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une MySQLError : %s", error4)
            print("connection_dbc.db.rollback() insertOneRecord")
        except pymysql.IntegrityError as error5:
            # MG 2020.03.23 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une IntegrityError : %s", error5)
            print("connection_dbc.db.rollback() insertOneRecord")
        except:
            # MG 2020.03.23 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print("Unknown error occurred")
        finally:
            print("C'est terminé....finally self.DBcursor.close()")
            self.DBcursor.close()