import os
import unittest
from config import basedir
from lumberjack import app, db

class TestHelper(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
[uckk4436885a]/home/chrycyna/NewFile.txt