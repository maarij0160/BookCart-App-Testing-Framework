import unittest
from pathlib import Path

if __name__ == "__main__":
    root_dir = Path('/Users/faheem/Book-Cart-App-Testing-Framework/')

    for dir_path in root_dir.glob('**/Tests*'):
        test_loader = unittest.TestLoader().discover(dir_path, pattern='UnitTests-Re*.py')
        unittest.TextTestRunner().run(test_loader)
