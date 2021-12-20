from flask import Blueprint, request
from app.main.services.standards import Output
from app.main.services.explore import Transactions
import json


stores_blueprint = Blueprint('stores', __name__)

version = '/v1.0'
exclusive_route = '/stores'
main_route = version + exclusive_route


@stores_blueprint.route(main_route, methods=["GET"])
def all_stores():
    '''
        :return:
        This endpoint return all stores names
    '''
    try:
        data = Transactions().get_stores()
        if data['status'] != 200:
            return Output().response_api(data['status'], data['results'])
        result = data['results'].to_json(orient='records')
        result = json.loads(result)
        return Output().response_api(200, result)
    except Exception as err:
        print('Error in get stores', err)
        return Output().response_api(500, None)



@stores_blueprint.route(main_route + '/transactions', methods=["GET"])
def transactions_by_stores():
    '''
        :return:
        This endpoint the transactions by stores
    '''
    try:
        data = Transactions().get_all_transactions()
        if data['status'] != 200:
            return Output().response_api(data['status'], data['results'])
        transactions_by_store = data['results'].to_json(orient='index')
        result = json.loads(transactions_by_store)
        return Output().response_api(200, result)
    except Exception as err:
        print('Error in get stores', err)
        return Output().response_api(500, None)