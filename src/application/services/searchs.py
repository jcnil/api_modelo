 # -*- coding: utf-8 -*-
#!/usr/bin/env python

class SearchCities:

    def search_cities(q,latitude,longitude,data_us,data_ca):

        usa_found = [cities for cities in data_us if q in cities['place_name'] and\
                     cities['latitude']<latitude and\
                     cities['longitude']<longitude]
        ca_found = [cities for cities in data_ca if q in cities['place_name'] and\
                     cities['latitude']<latitude and\
                     cities['longitude']<longitude]

        if len(usa_found)>0 or len(ca_found)>0:
            search = []
            for row in usa_found:
                resp_us = {"name":f"{row['place_name']},{row['state_code']},USA",\
                        "latitude":row['latitude'],\
                        "longitude":row['longitude'],\
                        "score": 0.0}
                search.append(resp_us)

            for row in ca_found:
                resp_ca = {"name":f"{row['place_name']},{row['state_code']},Canada",\
                        "latitude":row['latitude'],\
                        "longitude":row['longitude'],\
                        "score": 0.0}
                search.append(resp_ca)

            return {'search': search}

        else:
            return {'search': []}
