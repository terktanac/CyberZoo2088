import mysql.connector
from mysql.connector import Error


class Event():
    def __init__(self, data) :
        self.custDataObj = EventDB(data)
        
    def write(self) :
        return self.custDataObj.writeDB("testdb","test")
        
    def search(self) :
        return self.custDataObj.searchDB("testdb","test")
    
    def searchName(self) :
        return self.custDataObj.searchNameDB("testdb","test")

    def delete(self) :
        return self.custDataObj.deleteDB("testdb","test")

    def getInfo(self) :
        return self.custDataObj.data
    
class EventDB() :

    def __init__(self, data) :
        self.data = data


    def writeDB(self, databasename, table) :
        wdata=self.data

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database=databasename,
                                                 user='root',
                                                 password='terktana18')
       
            objdata = (wdata[0], wdata[1])
            
            sqlQuery = "insert into "+table+" (id, name) " \
                               "values (%s,%s)"
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            
            connection.commit()
            

        except:
            retmsg = ["1", "writing error"]
        else :
            retmsg = ["0", "writing done"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg

                

    #writeDB("testdb", "test", ["0007","Somsiri"])
                
    ##########################################################################

    def searchDB(self, databasename, table) :
        wkey = str(self.data[0])

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database=databasename,
                                                 user='root',
                                                 password='terktana18')
            objdata = (wkey,)
            sqlQuery = "select * from "+table+" where id = %s"
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            records = cursor.fetchone()
            self.data = records
                    
        except:
            retmsg = ["1", "Error"]
        else :
            retmsg = ["1", "Not Found"]
            if records[1] != "" :
                retmsg = ["0", "Found"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg


    ##########################################################################

    def searchNameDB(self, databasename, table) :
        wkey = str(self.data[1]) #correct here

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database=databasename,
                                                 user='root',
                                                 password='terktana18')
            objdata = (wkey,)
            sqlQuery = "select * from "+table+" where name = %s" #correct here
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            records = cursor.fetchone()
            self.data = records
                    
        except:
            retmsg = ["1", "Error"]
        else :
            retmsg = ["1", "Not Found"]
            if records[1] != "" :
                retmsg = ["0", "Found"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg

##########################################################################
    #homework start
    def deleteDB(self, databasename, table) :
        wkey = str(self.data[0])

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database=databasename,
                                                 user='root',
                                                 password='terktana18')
            objdata = (wkey,)
            sqlQuery = "Delete from "+table+" where id = %s"
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            connection.commit()
                    
        except:
            retmsg = ["1", "Error"]
        else :
            retmsg = ["0", "Delete Successful"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg
    #homework end



