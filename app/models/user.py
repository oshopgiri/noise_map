from app import mongo

class User():

    @classmethod
    def get(self):
        users = mongo.db.results.find()
        user_list = []
        for user in users:
            data = {}
            data['data'] = user['data']
            user_list.append(data)
        return user_list

    @classmethod
    def post(self):
        data = {"data":{"a": "b"}}
        results = mongo.db.results.insert_one(data)

    @classmethod
    def delete(self):
        query = {"data": {"a": "b"}}
        mongo.db.results.delete_many(query)
        
