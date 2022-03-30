 # -*- coding: utf-8 -*-
#!/usr/bin/env python


from flask import Flask, jsonify, request
from controller.config import config
from application.services import SearchCities,Suggestions
import json


app=Flask(__name__)


@app.route('/search', methods=['GET']) 
def search():

    q = request.args.get('q', type = str)
    latitude = request.args.get('latitude', type = float)
    longitude = request.args.get('longitude', type = float)

    try:
        with open(config['file_ca']) as file_ca:
            data_ca = json.load(file_ca)

        with open(config['file_us']) as file_us:
            data_us = json.load(file_us)
    except Exception as e:
        return {"Message": "Error to read file"}

    response = SearchCities.search_cities(q,latitude,longitude,data_us,data_ca)

    return jsonify(response)


@app.route('/suggestions', methods=['GET']) 
def suggestions():

    q = request.args.get('q', type = str)

    try:
        with open(config['file_ca']) as file_ca:
            data_ca = json.load(file_ca)

        with open(config['file_us']) as file_us:
            data_us = json.load(file_us)
    except Exception as e:
        return {"Message": "Error to read file"}

    response = Suggestions.search_suggestions(q,data_us,data_ca)

    return jsonify(response)


def page_not_found(error):
    return "Bad Request 404", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, page_not_found)
    app.run()
    
