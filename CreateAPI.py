# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 18:38:25 2020

@author: Daniel Camillo Rojas
"""

from flask import Flask
from flask_restx import Api, Resource, fields
from sklearn.externals import joblib

app = Flask(__name__)

api = Api(
    app, 
    version='1.0', 
    title='Predicting Price',
    description='Predicting Price')

ns = api.namespace('predict', 
     description='Predicting Price')
   
parser = api.parser()

parser.add_argument(
    'Model', 
    type=str, 
    required=True, 
    help='type Model', 
    location='args')

parser.add_argument(
    'Make', 
    type=str, 
    required=True, 
    help='Type make', 
    location='args')

parser.add_argument(
    'Mileage', 
    type=int, 
    required=True, 
    help='Type mileage', 
    location='args')

parser.add_argument(
    'Year', 
    type=int, 
    required=True, 
    help='Type year', 
    location='args')


parser.add_argument(
    'State', 
    type=str, 
    required=True, 
    help='type State', 
    location='args')

resource_fields = api.model('Resource', {
    'result': fields.String,
})

@ns.route('/')
class PredictingPrice(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
        Model = args['Model']
        Make = args['Make']
        Mileage = args['Mileage']
        Year = args['Year']
        State = args['State']
        
        #DF = DF.split('%3B')
        #print(DF)
        
        return {
         "result": PredictPrice(Model, Make, Mileage, Year, State)
        }, 200
        
app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)