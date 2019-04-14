# This is the module where the functions to manage the users data are written
import pymysql


# UserCheck
def get_all_user():
    sql = "SELECT id, name, surname FROM users"
    connection = pymysql.connect(user="root", password="", host="localhost", database='users')
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()


def add_user(id, name, surname, address, age, sex):
    sql = "INSERT INTO users(id,name,surname,address,age,sex) VALUES (%s,%s,%s,%s,%d,%s)", (id, name, surname, address, age, sex)
    connection = pymysql.connect(user="root", password="", host="localhost", database='users')
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
