import unittest
from app.print_colors import bcolors
from app.main import create_app

app = create_app('dev')

@app.cli.command('run')
def create_user():
    app.run()

@app.cli.command('test')
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        print(f"{bcolors.OKGREEN}>>>> Success! <<<<{bcolors.ENDC}")
        return 0
    else:
        print(f"{bcolors.FAIL}>>>> Fail! <<<<{bcolors.ENDC}")
        return 1