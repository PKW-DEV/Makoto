import sys

import mysql.connector
from mysql.connector import errorcode

config = {
    'host': "51.68.228.181",
    'user': "ksarbot",
    'password': "xwT878Dm2DdS",
    'database': "ksarbot",
    'raise_on_warnings': True

}


class DatabaseHandler():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Identifiants incorrect")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La DB existe pas")
            else:
                print(err)
################### GENSHIN #########################

    def check_if_user_exit(self, discord_user_id):
        self.con.connect()
        cursor = self.con.cursor()
        query = f"SELECT * FROM makoto_genshin WHERE discord_user_id = %s;"
        cursor.execute(query,(discord_user_id))
        result = cursor.fetchall()
        cursor.close()
        self.con.close()
        return len(result) == 1

    def add_user(self,username, ar, uid, discord_user_id):
        self.con.connect()
        cursor = self.con.cursor()
        query = f"INSERT INTO makoto_genshin (username, ar, uid, discord_user_id) VALUES (%s,%s,%s,%s);"
        cursor.execute(query, (username, ar, uid, discord_user_id))
        cursor.close()
        self.con.commit()
        self.con.close()

    def check_profil_user(self, discord_user_id):
        self.con.connect()
        cursor = self.con.cursor()
        query = f"SELECT * FROM makoto_genshin WHERE discord_user_id = %s;"
        cursor.execute(query,(discord_user_id))
        result = cursor.fetchall()
        cursor.close()
        self.con.close()
        return result

    def update_ar(self, ar, discord_user_id):
        self.con.connect()
        cursor = self.con.cursor()
        query = f"UPDATE makoto_genshin SET ar = %s WHERE discord_user_id = %s"
        cursor.execute(query,(ar, discord_user_id))
        cursor.close()
        self.con.commit()
        self.con.close()
        print("cc")
########################################################################################################################
    def add_help_genshin(self, ar, uid, user_id, why, voc, etat):
        self.con.connect()
        cursor = self.con.cursor()
        query = f"INSERT INTO makoto_genshin_help (ar,uid,user_id,why,voc,etat) VALUES (%s,%s,%s,%s,%s,%s);"
        cursor.execute(query,(ar, uid, user_id, why, voc, etat))
        cursor.close()
        self.con.commit()
        self.con.close()

    def check_if_user_need_help(self, user_id):
        self.con.connect()
        cursor = self.con.cursor()
        query = f"SELECT * FROM makoto_genshin_help WHERE user_id = %s;"
        cursor.execute(query,(user_id))
        result = cursor.fetchall()
        cursor.close()
        self.con.close()
        return len(result) == 0
    

########################################################################################################################
    def add_message(self,servname, servid, messid, chanid):
        self.con.connect()
        cursor = self.con.cursor()
        query = f"INSERT INTO makoto_rolebutton_serv (servname, servid, messid, chanid) VALUES (%s,%s,%s);"
        cursor.execute(query,(servname, servid, messid, chanid))
        cursor.close()
        self.con.commit()
        self.con.close()
        print("MAKOTO | add new message for role menu")

    def get_message(self, servid ):
        self.con.connect()
        cursor = self.con.cursor()
        query = f"SELECT messid FROM makoto_rolebutton_serv WHERE servid = %s;"
        cursor.execute(query,(servid))
        result = cursor.fetchall()
        cursor.close()
        self.con.close()
        return result

    def get_channel(self, servid ):
        self.con.connect()
        cursor = self.con.cursor()
        query = f"SELECT chanid FROM makoto_rolebutton_serv WHERE servid = %s;"
        cursor.execute(query,(servid))
        result = cursor.fetchall()
        cursor.close()
        self.con.close()
        return result
