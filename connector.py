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
            database='test',
            user='root',
            password='tongplw'
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
            database='test',
            user='root',
            password='tongplw'
        )

        for key, val in kwargs.items():
            attr = key
            value = val

        sql_query = "DELETE FROM {table} WHERE {attr}='{val}';".format(
            table=table,
            attr=attr,
            val=value
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
    pass

# print(insert('animal', AnimalID='4', Nickname='AA', Gender='F'))
# delete('animal', AnimalID=1)