import os
import tempfile
import unittest

from controller.app import app

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.config.update(
            TESTING=True,
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )

    