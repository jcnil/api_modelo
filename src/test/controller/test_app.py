from unittest.mock import patch

from expects import (
    equal,
    expect
)

from test import BaseTestCase

class SearchEndpointTestCase(BaseTestCase):

    def test_endpoint_status_can_be_checked(self):
        response = self.client.get('/search?q=Londo&latitude=43.70011&longitude=-79.4163')

        expect(response.status_code).to(equal(200))
        expect(response.json).to(equal({'status': 'alive!'}))

class SuggestionsEndpointTestCase(BaseTestCase):

    def test_endpoint_status_can_be_checked(self):
        response = self.client.get('/suggestions?q=SomeRandomCityInTheMiddleOfNowhere')

        expect(response.status_code).to(equal(200))
        expect(response.json).to(equal({'status': 'alive!'}))