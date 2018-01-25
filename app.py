# -*- coding: utf-8 -*-
"""
Author: D.Fitzgerald

"""
from flask import Flask, request, json
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

#Create a engine for connecting to SQLite3.
e = create_engine('sqlite:////Users/desfi/Documents/Distilled_SCH/my_sqlite.db')

app = Flask(__name__)
api = Api(app)

class car(Resource):
    def get(self):
        conn = e.connect() # connect to database
        query = conn.execute("select make,model,year,id,last_updated,price from carTable") # This line performs query and returns json result
        result = {'cars': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result
    
    def post(self):
        conn = e.connect()
        print(request.json)
        make = request.json['make']
        model= request.json['model']
        year = request.json['year']
        chassis_id = request.json['chassis_id']
        id = request.json['id']
        last_updated = request.json['last_updated']
        price = request.json['price']
        query = conn.execute("insert into carTable values(null,'{0}','{1}','{2}','{3}','{4}', \
                                                          '{5}','{6}')".format(make,model,year,chassis_id,id,last_updated,price))
        return {'Created'}
    
class id(Resource):
    def get(self, id):
        conn = e.connect()
        query = conn.execute("select make,model,year,id,last_updated,price from carTable where id=%s" % id)
        result = {'id': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result
        
class avgPrice(Resource):
    def post(self):
        conn = e.connect()
        make = request.json['make']
        model= request.json['model']
        year = request.json['year']
        chassis_id = request.json['chassis_id']
        id = request.json['id']
        last_updated = request.json['last_updated']
        price = request.json['price']

        query = conn.execute("select avg(price) from carTable where ((make = '{0}') and (model = '{1}') and (year = '{2}')) ")
        return {'avg_price': [i[0] for i in query.cursor.fetchall()]}
  
api.add_resource(car, '/car')
api.add_resource(id, '/car/<int:id>')
api.add_resource(avgPrice, '/avgprice')


@app.route("/car")
def index():
    return "Method used %s" % request.method

if __name__ == '__main__':
     app.run()
