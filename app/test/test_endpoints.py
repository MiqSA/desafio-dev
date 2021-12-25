import json
import unittest
from flask_testing import TestCase
from app.print_colors import bcolors
from app.manage import app
from app.main.config import API_VERSION, basedir
import os
from io import StringIO


print('[ 3 ] - ENDPOINTS TESTS')

class UsersEndpointsTestCase(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.DevelopmentConfig')
        return app

    def test_upload_endpoint(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        file_path = basedir + '/files/CNAB.txt'

        resp = app.test_client().post('/v1.0/files/upload',
                                      data={'myFile': (file_path, 'CNAB.txt')},
                                      follow_redirects=True)
        self.assertEquals(resp.status, "200 OK")


    def response_by_method(self, route, method, data=None, status=200):
        # print(route)
        if route == '/static/<path:filename>':
            print(f"{bcolors.WARNING}'{route}  >>> Not implemented yet!'{bcolors.ENDC}")
            pass
        else:
            # When
            if method == 'GET':
                response = app.test_client().get(route, headers={"Content-Type": "application/json"}, json=data)
            elif method == 'POST':
                response = app.test_client().post(route, headers={"Content-Type": "application/json"},
                                                  json=data)
            # Then
            self.assertEqual(str, type(response.json['message']))
            self.assertEqual(list, type(response.json['results']))
            self.assertEqual(int, type(response.json['status']))
            self.assertEqual(status, response.status_code)
            print(f"{bcolors.OKBLUE}'{route} >>> ok!'{bcolors.ENDC}")

    def test_endpoints(self):

        # Endpoints List
        all_routes = {'GET':[], 'POST':[]}
        for route in self.app.url_map.iter_rules():
            if 'GET' in route.methods:
                all_routes['GET'].append(str(route))
            elif 'POST' in route.methods:
                all_routes['POST'].append(str(route))


        print('\n')
        # Testing endpoints with method GET
        for route in all_routes['GET']:
            if API_VERSION in route:
                self.response_by_method(route, 'GET')


if __name__ == '__main__':
    unittest.main()