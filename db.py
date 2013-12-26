import MySQLdb
from MySQLdb.cursors import DictCursor

class DBClass:
    def __init__(self, **kwargs):
        self.base = kwargs.get('base')
        self.user = kwargs.get('user')
        self.password = kwargs.get('password')
        self.host = kwargs.get('host')

        self.db = MySQLdb.connect(host=self.host,
                             user=self.user,
                             passwd=self.password,
                             db=self.base,
                             cursorclass=DictCursor)

        self.cursor = self.db.cursor()

    def select(self, table, *args, **kwargs):
        """
        
        """
        # what values need select
        selected = '*' if not args else ', '.join([arg for arg in args])
        
        sql = 'SELECT {selected} FROM {table}'.format(table=table, selected=selected)
        
        if kwargs:
        # format kwargs into sql format
            where = ['{key}="{value}"'.format(key=key, value=value) for key, value in kwargs.iteritems()]
            where = ' WHERE' +' AND '.join(where)
            sql += where           
     
        self.cursor.execute(sql)

        return self.cursor.fetchall()

    def insert(self, table, **kwargs):
        """

        """
        field_names = ', '.join(kwargs.keys())

        values = '"'+'", "'.join(kwargs.values()) + '"'

        sql = 'INSERT INTO {table}({field_names}) VALUES({values})'.format(table=table,
                                                                    field_names=field_names,
                                                                    values=values)

        self.cursor.execute(sql)
        self.db.commit()
        return self.cursor.fetchall()


    def delete(self, table, **kwargs):
        """
        """
        # format kwargs into sql format
        where = ['{key}="{value}"'.format(key=key, value=value) for key, value in kwargs.iteritems()]

        sql = 'DELETE FROM {table} WHERE {where}'.format(table=table, where=' AND '.join(where))       
        self.cursor.execute(sql)
        self.db.commit()
        return self.cursor.fetchall()







db = DBClass(base='test', user='root', password='qazedc', host='localhost')

#db.delete('users', fname='Ivan')
#db.insert('users', fname='Ivan', lname='Ivanov', nickname='ivanko')
print db.select('users')