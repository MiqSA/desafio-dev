# Blueprints
from app.main.resources.stores.stores import stores_blueprint
from app.main.resources.files.files import files_blueprint
from app.main.resources.pages.pages import pages_blueprint


class Endpoints(object):
     def __init__(self, app):
         self.app = app


     def availables(self):
        self.app.register_blueprint(stores_blueprint)
        self.app.register_blueprint(files_blueprint)
        self.app.register_blueprint(pages_blueprint)
        return self.app