 # -*- coding: utf-8 -*-
#!/usr/bin/env python

from expects import (
    equal,
    expect,
    contain
)

from application.services import SearchCities,Suggestions
from test import BaseTestCase


class SearchCitiesTestCase(BaseTestCase):

    def test_it_rerturns_search(self):
        
        q = 'Londo'
        latitude = 43.70011
        longitude = -79.4163

        data_us = {
            "country_code": "US",
            "postal_code": 3257,
            "place_name": "New London",
            "state_name": "New Hampshire",
            "state_code": "NH",
            "county_name": "Merrimack",
            "county_code": 13,
            "community_name": null,
            "community_code": null,
            "latitude": 43.4145,
            "longitude": -71.9857,
            "accuracy": 4
            }

        data_ca = {
            "country_code": "CA",
            "postal_code": "N5V",
            "place_name": "London (YXU / North and East Argyle / East Huron Heights)",
            "state_name": "Ontario",
            "state_code": "ON",
            "county_name": "London",
            "county_code": null,
            "community_name": null,
            "community_code": null,
            "latitude": 43.0233,
            "longitude": -81.1643,
            "accuracy": 1
            }

        result = SearchCities().search_cities(
                        q,\
                        latitude,\
                        longitude,\
                        data_us,\
                        data_ca)

        expect(result['latitude']).to(equal(latitude))
        expect(result['longitude']).to(equal(longitude))
        expect(result['name']).to(contain(q))

class SuggestionsTestCase(BaseTestCase):

    def test_it_rerturns_suggestion(self):

        q = 'SomeRandomCityInTheMiddleOfNowhere'
        
        data_us = {}
        data_ca = {}
        
        result = Suggestions().search_suggestions(
                        q,\
                        data_us,\
                        data_ca)

        expect(result['name']).to(contain(q))