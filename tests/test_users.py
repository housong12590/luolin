import unittest
from tests import app


class UserModelCase(unittest.TestCase):

    def setUp(self):
        self.app_context = self.app_context()
        self.app_context.push()

    def tearDown(self):
        pass
