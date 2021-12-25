import json
import unittest
from flask_testing import TestCase
from app.print_colors import bcolors
from app.manage import app
from app.main.config import API_VERSION

print('[ 2 ] - PAGES TESTS')

class UsersEndpointsTestCase(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.DevelopmentConfig')
        return app

    def test_upload_page(self):
        app.test_client().get('/upload')
        self.assert_template_used('uploads.html')

    def test_home_page(self):
        app.test_client().get('/')
        self.assert_template_used('home.html')


if __name__ == '__main__':
    unittest.main()