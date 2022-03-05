import mysql.connector

SQL_HOST = "sql11.freemysqlhosting.net"
SQL_USER = "sql11477106"
SQL_PASS = "DpbezX8H85"
SQL_DB = "sql11477106"

class DB:
    @staticmethod
    def connect():
        return mysql.connector.connect(
            host=SQL_HOST,
            user=SQL_USER,
            passwd=SQL_PASS,
            database=SQL_DB
        )

    @staticmethod
    def query(query, *args):
        if query.upper().startswith("SELECT"):
            return DB.query_return(query, *args)

        con = DB.connect()
        cursor = con.cursor()

        cursor.execute(query, *args)
        con.commit()

        if query.upper().startswith("INSERT"):
            ret = cursor.lastrowid
        else:
            ret = None

        cursor.close()
        con.close()

        return ret


    @staticmethod
    def query_return(query, *args):
        con = DB.connect()
        cursor = con.cursor()

        cursor.execute(query, *args)
        ret = cursor.fetchall()

        cursor.close()
        con.close()

        return ret


if __name__ == "__main__":
    # Reset everything
    DB.query("DROP TABLE zoo")
    DB.query("DROP TABLE logs")
    DB.query("CREATE TABLE zoo(id INT PRIMARY KEY AUTO_INCREMENT, animal TEXT, gender TEXT, subtype TEXT, age INT, color TEXT)")
    DB.query("CREATE TABLE logs(id INT PRIMARY KEY AUTO_INCREMENT, date TEXT, animalid INT, comment TEXT)")
    DB.query("INSERT INTO zoo VALUES(%s, %s, %s, %s, %s, %s)", (None, "giraffe", "female", "africane", 20, "red"))
    DB.query("INSERT INTO zoo VALUES(%s, %s, %s, %s, %s, %s)", (None, "rhino", "female", "africane", 7, "red"))
    DB.query("INSERT INTO zoo VALUES(%s, %s, %s, %s, %s, %s)", (None, "rhino", "male", "africane", 3, "yellow"))
    DB.query("INSERT INTO zoo VALUES(%s, %s, %s, %s, %s, %s)", (None, "lion", "male", "jamaican", 10, "red"))
    DB.query("INSERT INTO zoo VALUES(%s, %s, %s, %s, %s, %s)", (None, "lion", "female", "jamaican", 7, "brown"))