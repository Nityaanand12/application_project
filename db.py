def connect():
    import psycopg2
    import json
    f = open('config.json')
    data = json.load(f)
    database = data.get('database')
    con = psycopg2.connect(dbname=database.get('dbname'),user=database.get('user'),password=database.get("password"),host=database.get("host"),port= database.get('port'))
    return con,con.cursor()
def insert(user):
    con,cur = connect()
    cur.execute("insert into customers(user1) values('%s')" %user)
    con.commit()
    con.close()
    return 'successfully inserted'
def delete(id, name):
    con,cur = connect()
    cur.execute("delete from customers where id=%s and user1='%s' " %(id,name))
    con.commit()
    con.close()
    return 'successfully deleted'
def update(id, name):
    con,cur = connect()
    cur.execute("update customers set user1='%s' where id = '%s'" %(name,id))
    con.commit()
    con.close()
    return 'successfully updated'
def report():
    con,cur = connect()
    cur.execute("select * from customers")
    data = cur.fetchall()
    con.close()
    return data
def create_table():
    con,cur = connect()
    cur.execute("create table customers(id serial primary key, user1 varchar(255))")
    cur.execute("create table users(id serial primary key, user1 varchar(255),password varchar(255))")
    con.commit()
    con.close()
def insert_user_register(name, password):
    con,cur = connect()
    cur.execute("insert into users(user1,password) values('%s','%s')" %(name, password))
    con.commit()
    con.close()
    return 'successfully registered'
def browse_user(name,password):
    con,cur = connect()
    cur.execute("select * from users where user1='%s' and password='%s'" %(name,password))
    data = cur.fetchone()
    con.close()
    return data
if __name__ == '__main__':
    create_table()