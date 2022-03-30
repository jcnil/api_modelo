 # -*- coding: utf-8 -*-
#!/usr/bin/env python

class Suggestions:

    def search_suggestions(q,data_us,data_ca):

        usa_found = [cities for cities in data_us if q in cities['place_name']]
        ca_found = [cities for cities in data_ca if q in cities['place_name']]

        if len(usa_found)>0 or len(ca_found)>0:
            suggestions = []
            for row in usa_found:
                resp_us = {"name":f"{row['place_name']},{row['state_code']},USA",\
                        "latitude":row['latitude'],\
                        "longitude":row['longitude'],\
                        "score": 0.0}
                suggestions.append(resp_us)

            for row in ca_found:
                resp_ca = {"name":f"{row['place_name']},{row['state_code']},Canada",\
                        "latitude":row['latitude'],\
                        "longitude":row['longitude'],\
                        "score": 0.0}
                suggestions.append(resp_ca)

            return {'search': suggestions}
        else:
            return {'search': []}