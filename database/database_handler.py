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

    def add_message(self,servname, servid, messid):
        self.con.connect()
        cursor = self.con.cursor()
        query = f"INSERT INTO makoto_rolebutton_serv (servname, servid, messid) VALUES (%s,%s,%s);"
        cursor.execute(query,(servname, servid, messid))
        cursor.close()
        self.con.commit()
        self.con.close()
        print("MAKOTO | add new message for role menu")

    def get_message(self, servid):
        self.con.connect()
        cursor = self.con.cursor()
        query = f"SELECT messid FROM makoto_rolebutton_serv WHERE servid = %s;"
        cursor.execute(query,(servid))
        result = cursor.fetchall()
        cursor.close()
        self.con.close()
        return result