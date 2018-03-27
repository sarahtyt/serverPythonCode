import pyodbc

SERVER = 'bulubulu.ischool.uw.edu'
DATABASE = 'YVYC'
USERNAME = 'sa'
PASSWORD = 'GoTeam2018!'

def execute(sql):
    conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+SERVER+';PORT=1433;DATABASE='+DATABASE+';UID='+USERNAME+';PWD='+ PASSWORD)
    cursor = conn.cursor()
    cursor.execute(sql)

    results = list(cursor.fetchall())

    conn.close()
    return results