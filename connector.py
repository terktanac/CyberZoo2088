import mysql.connector
from mysql.connector import Error

password = 'terktana18'
database = 'cyberzoo2088'

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
            database=database,
            user='root',
            password=password
        )

        params = ''
        values = ''
        for key, val in kwargs.items():
            params += key + ','
            if val == '':
                values += "null,"
            else:
                values += "'{val}',".format(val=val)
            
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
        ret_msg = ["0", "Completed ID = " + str(cursor.lastrowid)]
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()

    return ret_msg



def delete(table, **kwargs):

    try:
        connection = mysql.connector.connect(
            host='localhost',
            database=database,
            user='root',
            password=password
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



def select(table, one_row=True, command=None, **kwargs):
    
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database=database,
            user='root',
            password=password
        )

        if command == None:
            cond = ''
            for key, val in kwargs.items():
                cond += "{key}='{val}',".format(key=key, val=val)

            sql_query = "SELECT * FROM {table} WHERE {cond};".format(
                table=table,
                cond=cond[:-1]
            )
        else:
            sql_query = command
        
        cursor = connection.cursor()
        cursor.execute(sql_query)
        if one_row:
            records = {k:v if v else '' for k, v in zip(cursor.column_names, cursor.fetchone())}
        else:
            records = [list(cursor.column_names)] + cursor.fetchall()
            

    except:
        ret_msg = ["1", "Error"]
    else:
        ret_msg = ["1", "Not Found"]
        if records != None :
            ret_msg = ["0", "Completed", records]
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()

    return ret_msg


def update(table, pk, pk_val, **kwargs):

    try:
        connection = mysql.connector.connect(
            host='localhost',
            database=database,
            user='root',
            password=password
        )

        values = ''
        for key, val in kwargs.items():
            if val != '':
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



# print(insert('animal', ABDate='1999-1-1', AType='AA', Gender='F', HabitatID='1', ParentID=''))
# delete('zoo_event', EventID=1)
# insert('zoo_event', EDate='1999-2-2', EName='A', ETime='09:10:00', ZName='HOT')
# print(select('zoo_event', EventID='6'))
# print(select('zoo_event', EName='AA', one_row=False))
# print(update('zoo_event', 'EventID', '6', EDate='1999-2-2', EName='AAA', ETime='09:10:00', ZName='HOTTTT'))
# print(insert('zoo_event', EDate='1999-1-1',EName='AA', ETime='8:8:8', ZName='AAA', SFlag=1, NID=1, EFlag=0))