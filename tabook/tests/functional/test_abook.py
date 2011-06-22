from tabook.tests import *

class TestAbookController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='abook', action='index'))
        # Test response...
