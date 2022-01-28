import psycopg2
import numpy as np

def column_stats(table_name,column_name):
    conn=psycopg2.connect(dbname='db')
    cursor=conn.cursor()
    cursor.execute(" select "+column_name+" from "+table_name+";")
    records=np.array(cursor.fetchall())
    return np.mean(records),np.median(records)
