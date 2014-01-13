from pymongo import MongoClient
import json

class User():
    def __init__(self, **kwargs):
        self.fname = kwargs.get('fname', '')
        self.lname = kwargs.get('lname', '')
        self.password = kwargs.get('password', '')


class MongoWrapper():
    def __init__(self, **kwargs):
		#
        if 'uri' in kwargs:
            self.client = MongoClient(kwargs['uri'])            
        else:
            self.client = MongoClient(kwargs.get('host', 'localhost'),
                                      kwargs.get('port', 27017))
        #
        if 'db' in kwargs:			
            self.db = self.client[kwargs.get('db')]
     
            self.collection = self.db[kwargs.get('collection')]
        
    def switch_collection(self, collection):
        self.collection = collection
    
    def select(self):
        cursor = self.collection.find()
        return [item for item in cursor]

    def delete(self, object):
        self.collection.remove(object)
	    
    def update(self, prev_object, present_object):
        self.collection.update(prev_object, present_object, multi=True)
        
    def insert(self, object):
        self.collection.insert(object, safe=True)
        
    def check(self, object):
        return self.collection.find(object).count() > 0
        
    


if __name__ == '__main__':    
    #db = MongoWrapper(uri='mongodb://localhost:27017/test_db')
    db = MongoWrapper(host='localhost', port=27017, db='test_db',
                       collection='users')
    
    #user = User(fname='bla')
    #db2.insert(user)
    print db.select()
    
    
    

