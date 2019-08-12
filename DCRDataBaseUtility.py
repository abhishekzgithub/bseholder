import pymysql.cursors
import sqlite3 as sql
import collections


def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data
def db_query(query, fields=None, multiple_flag=None):
    '''
    Get the data from the database.
    '''

    conn = pymysql.connect(host='stocksdb.cfr9lpwixl2c.ap-south-1.rds.amazonaws.com',
                                user='kingsd',
                                password='Guitar12',
                                db='stocksdb',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    # conn = sql.connect(database)
    conn.row_factory = sql.Row

    if multiple_flag == None:
        multiple_flag = True
    else:
        multiple_flag = False

    cur = conn.cursor()
    if fields:
        cur.execute(query, tuple(fields))
    else:
        cur.execute(query)
    if multiple_flag:
        rows = cur.fetchall()
    else:
        rows = cur.fetchone()

    conn.close()
    
    # rows = convert(rows)

    return rows
def db_commit_query(query, fields=None):
    '''
    Get the data from the database.
    '''

    conn = pymysql.connect(host='stocksdb.cfr9lpwixl2c.ap-south-1.rds.amazonaws.com',
                                user='kingsd',
                                password='Guitar12',
                                db='stocksdb',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    # conn = sql.connect(database)
    conn.row_factory = sql.Row

    cur = conn.cursor()
    if fields:
        cur.execute(query, tuple(fields))
    else:
        cur.execute(query)

    conn.commit()
    conn.close()
    return
def db_json(query, fields=None, database=None):
    rows = db_query(query, fields, database)
    jsonList = []
    for data in rows:
        jsonList.append(data)
    return jsonList


def db_commit_query_id(query, fields=None):
    '''
    Get the data from the database.
    '''
    
    conn = pymysql.connect(host='stocksdb.cfr9lpwixl2c.ap-south-1.rds.amazonaws.com',
                                user='kingsd',
                                password='Guitar12',
                                db='stocksdb',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    # conn = sql.connect(database)
    conn.row_factory = sql.Row

    cur = conn.cursor()
    if fields:
        cur.execute(query, tuple(fields))
    else:
        cur.execute(query)

    entered_key = cur.lastrowid
    conn.commit()
    conn.close()
    return entered_key

