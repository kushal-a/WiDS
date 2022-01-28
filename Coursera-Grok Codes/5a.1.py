import psycopg2
def select_all(tableName):
    conn=psycopg2.connect(dbname='db')
    cursor=conn.cursor()
    cursor.execute("select * from "+tableName)
    return cursor.fetchall()
