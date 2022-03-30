# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os

class DevelopmentConfig():
    DEBUG =  True


config={
    'development' :  DevelopmentConfig,
    'file_us':'../infrastructure/data/US_final.json',
    'file_ca':'../infrastructure/data/CA_final.json'
}

