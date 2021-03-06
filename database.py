import sqlite3

conn = sqlite3.connect('SqliteDB.db')
cursor = conn.cursor()


class DatabaseManager:
    @staticmethod
    def createTables():
        if len(cursor.execute("""SELECT name FROM sqlite_master WHERE type='table';""").fetchall()) == 0:
            cursor.execute("""create table users(
            id integer primary key,
            login text unique,
            password text
            )""")
            cursor.execute("""create table sessions(
            id integer primary key,
            login text,
            token text
            )""")
            cursor.execute("""create table controllers(
            id integer primary key,
            name text,
            userId integer,
            encoding text,
            buttons text
            )""")
            cursor.execute("""create table scripts(
            id integer primary key,
            name text,
            userId integer,
            sequence text
            )""")
        conn.commit()

    @staticmethod
    def clearTable(tableName):
        cursor.execute("delete * from '{tableName}'".format(tableName=tableName))
        conn.commit()

    @staticmethod
    def addUser(login, password):
        cursor.execute("insert into users(login, password) "
                       "values ('{login}' , '{password}')"
                       .format(login=login, password=password))
        conn.commit()

    @staticmethod
    def addScript(name, userId, sequence):
        cursor.execute("insert into scripts(name, userId, sequence)"
                       "values ('{name}', '{userId}', '{sequence}')"
                       .format(name=name, userId=userId, sequence=sequence))
        conn.commit()

    @staticmethod
    def addController(name, userId, encoding, buttons):
        cursor.execute("insert into controllers(name, userId, encoding, buttons)"
                       "values ('{name}', '{userId}', '{encoding}', '{buttons}')"
                       .format(name=name, userId=userId, encoding=encoding, buttons=buttons))
        conn.commit()

    @staticmethod
    def addSession(login, token):
        cursor.execute("insert into sessions(login, token)"
                       "values('{login}', '{token}')"
                       .format(login=login, token=token))
        conn.commit()

    @staticmethod
    def updateUser(id, login, password):
        cursor.execute("update users set login='{login}', "
                       "password='{password}' where id='{id}'"
                       .format(id=id, login=login, password=password))
        conn.commit()

    @staticmethod
    def updateController(name, userId, buttons):
        cursor.execute("update controllers set buttons='{buttons}' where name='{name}' and userId='{userId}'"
                       .format(buttons=buttons, name=name, userId=userId))
        conn.commit()

    @staticmethod
    def deleteUser(login):
        cursor.execute("delete from users where login='{login}'".format(login=login))
        conn.commit()

    @staticmethod
    def deleteController(name, userId):
        cursor.execute("delete from controllers where name='{name}' and userId='{userId}'"
                       .format(name=name, userId=userId))
        conn.commit()

    @staticmethod
    def getUsers():
        cursor.execute("select * from users")
        conn.commit()
        return cursor.fetchall()

    @staticmethod
    def checkUser(login):
        cursor.execute("select * from users where login='{login}'".format(login=login))
        conn.commit()
        return cursor.fetchall()

    @staticmethod
    def getUser(login, password):
        cursor.execute("select * from users where login='{login}' and password='{password}'"
                       .format(login=login, password=password))
        conn.commit()
        return cursor.fetchall()

    @staticmethod
    def getUserId(login):
        cursor.execute("select id from users where login='{login}'"
                       .format(login=login))
        conn.commit()
        return cursor.fetchone()[0]

    @staticmethod
    def getScript(id):
        cursor.execute("select sequence from scripts where id='{id}'".format(id=id))
        conn.commit()
        return cursor.fetchone()

    @staticmethod
    def getUserControllers(userId):
        cursor.execute("select * from controllers where userId='{userId}'".format(userId=userId))
        conn.commit()
        return cursor.fetchall()

    @staticmethod
    def checkSession(token):
        cursor.execute("select login from sessions where token='{token}'".format(token=token))
        conn.commit()
        return cursor.fetchall != 0
