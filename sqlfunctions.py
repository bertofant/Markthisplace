import psycopg2

CONFIGDBSTRING = "dbname='kclxalbu' user='kclxalbu' password='VKrYKg1EJfFTF4ydqWV5TBhBsBLWun6u' host='kandula.db.elephantsql.com'  "


def create_config_table():
    conn = psycopg2.connect(CONFIGDBSTRING)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS config (username TEXT, name TEXT, password TEXT)")
    conn.commit()
    conn.close()

def insert_in_config_table(username,name,password):
    conn = psycopg2.connect(CONFIGDBSTRING)
    cur = conn.cursor()
    cur.execute(f"INSERT INTO config VALUES ('{username}', '{name}', '{password}')")
    conn.commit()
    conn.close()

def view_config_table():
    conn = psycopg2.connect(CONFIGDBSTRING)
    cur = conn.cursor()
    cur.execute("SELECT * FROM config")
    rows =  cur.fetchall()
    conn.close()
    return rows

def delete_from_config_table(username):
    conn = psycopg2.connect(CONFIGDBSTRING)
    cur = conn.cursor()
    cur.execute("DELETE FROM config WHERE username=%s",(username,))
    conn.commit()
    conn.close()

def update_in_config_table(usernmane,name,password):
    conn = psycopg2.connect(CONFIGDBSTRING)
    cur = conn.cursor()
    cur.execute("UPDATE config SET name=%s, password=%s WHERE username=%s",(name, password, usernmane) )
    conn.commit()
    conn.close()



def getconfigfromsql():
    config = {}
    config['cookie'] = {'expiry_days': 30, 'key': 'webapp_presenze_key', 'name':'webapp_presenze_name' }
    credentials_dict={}
    usernames_dict={}
    accounts = view_config_table()
    for account in accounts:
        usernames_dict[account[0]]={'email': account[0], 'name': account[1], 'password': account[2] }
    credentials_dict['usernames'] = usernames_dict

    config['credentials']=credentials_dict
    preauth_dict = {}
    preauth_dict['emails'] = None
    config['preauthorized'] = preauth_dict
    return config

