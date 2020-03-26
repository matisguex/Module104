# insert_table_values.py
# MG 2020.03.23 essai d'insertion

import connect_db
# Importer le fichier "InsertOneTable" dans lequel il y a quelques classes et méthodes en rapport avec le sujet d'insertion dans UNE SEULE table.
from INSERT import insert_one_table

try:


    # MG 2020.03.23 Démonstration en classe, juste pour faire un objet "jeveux_etre_connecte"

    objet_etre_connecte = connect_db.DatabaseTools()

    # MG 2020.03.23 Une instance "insert_records" pour permettre l'utilisation des méthodes de la classe DbInsertOneTable
    insert_records = insert_one_table.DbInsertOneTable()

    valeur_nom = "Guex"
    valeur_prenom = "Matis"
    valeur_date_naissance = "06.11.2003"
    print(valeur_nom)
    print(valeur_prenom)
    print(valeur_date_naissance)


    insert_records.insert_one_record_one_table("INSERT IGNORE INTO t_personnes (id_personne, intitule_Nom_personne) VALUES (null, %(values_insert)s)",valeur_nom)
    insert_records.insert_one_record_one_table("INSERT IGNORE INTO t_personnes (id_personne, intitule_Prenom_personne) VALUES (null, %(values_insert)s)",valeur_prenom)
    insert_records.insert_one_record_one_table("INSERT IGNORE INTO t_personnes (id_personne, intitule_DateNaissance_personne) VALUES (null, %(values_insert)s)",valeur_date_naissance)

    objet_etre_connecte.close_connection()
except Exception as erreur_de_merde:
    print("il y a une erreur {0}",erreur_de_merde)