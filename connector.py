import mysql.connector
from mysql.connector import Error



def insert(table, **kwargs):
    """ FOR EXAMPLE

        insert(
            'zoo_event', 
            EDate = '1999-2-2',
            EName = 'Happy Birthday',
            ETime = '09:10:00',
            ZName = 'Desert'
        )
    """
    
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='cyberzoo2088',
            user='root',
            password='terktana18'
        )

        params = ''
        values = ''
        for key, val in kwargs.items():
            params += key + ','
            values += "'" + val + "',"

        sql_query = "INSERT INTO {table} ({params}) VALUES ({values});".format(
            table=table,
            params=params[:-1],
            values=values[:-1]
        )
        
        cursor = connection.cursor()
        cursor.execute(sql_query)
        connection.commit()
    except:
        ret_msg = ["1", "Error"]
    else:
        ret_msg = ["0", "Completed"]
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()

    return ret_msg



def delete(table, **kwargs):

    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='cyberzoo2088',
            user='root',
            password='terktana18'
        )
        
        cond = ''
        for key, val in kwargs.items():
            cond += "{key}='{val}'".format(key=key, val=val)

        sql_query = "DELETE FROM {table} WHERE {cond};".format(
            table=table,
            cond=cond
        )
        
        cursor = connection.cursor()
        cursor.execute(sql_query)
        connection.commit()
                
    except:
        ret_msg = ["1", "Error"]
    else:
        ret_msg = ["0", "Completed"]
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()

    return ret_msg



def select(table, **kwargs):
    
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='cyberzoo2088',
            user='root',
            password='terktana18'
        )

        cond = ''
        for key, val in kwargs.items():
            cond += "{key}='{val}',".format(key=key, val=val)

        sql_query = "SELECT * FROM {table} WHERE {cond};".format(
            table=table,
            cond=cond[:-1]
        )
        
        cursor = connection.cursor()
        cursor.execute(sql_query)
        records = {k:v for k, v in zip(cursor.column_names, cursor.fetchone())}
    except:
        ret_msg = ["1", "Error"]
    else:
        ret_msg = ["1", "Not Found"]
        if records != None :
            ret_msg = ["0", "Complete", records]
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()

    return ret_msg


def update(table, pk, pk_val, **kwargs):

    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='cyberzoo2088',
            user='root',
            password='terktana18'
        )

        values = ''
        for key, val in kwargs.items():
            values += "{key}='{val}',".format(key=key, val=val)

        sql_query = "UPDATE {table} SET {values} WHERE {cond};".format(
            table=table,
            values=values[:-1],
            cond='{pk}={pk_val}'.format(pk=pk, pk_val=pk_val)
        )
        
        cursor = connection.cursor()
        cursor.execute(sql_query)
        connection.commit()
                
    except:
        ret_msg = ["1", "Error"]
    else:
        ret_msg = ["0", "Completed"]
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()

    return ret_msg

# print(insert('animal', AnimalID='7', Nickname='AA', Gender='F'))
# delete('zoo_event', EventID=1)
# insert('zoo_event', EDate='1999-2-2', EName='A', ETime='09:10:00', ZName='HOT')
# print(select('zoo_event', EventID='6'))
# print(update('zoo_event', 'EventID', '6', EDate='1999-2-2', EName='AAA', ETime='09:10:00', ZName='HOTTTT'))