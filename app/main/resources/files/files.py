from flask import Blueprint, request, url_for, redirect
from app.main.services.standards import Output
from app.main.services.manage_files import CRUD
from app.main.config import basedir
import os


files_blueprint = Blueprint('files', __name__)
_basedir_files = basedir + '/databases/datafiles/'


version = '/v1.0'
exclusive_route = '/files'
main_route = version + exclusive_route


@files_blueprint.route(main_route + '/upload', methods=["POST"])
def upload_file():
    try:
        file = request.files.get("myFile")
        file.save(os.path.join(_basedir_files, file.filename))
        if '.txt' not in file.filename:
            return Output().response_api(403, 'Choose a valid file .txt')
        CRUD(filename=f'{_basedir_files}/{file.filename}').main()
        return redirect(url_for('pages.index'))
    except Exception as err:
        print('Error in  upload files', err)
        return Output().response_api(500, None)



