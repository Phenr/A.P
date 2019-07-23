#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import hashlib
import os

class interface():
    def __init__(self):
        self.u = "b1475789ac318f798cdcc63f742af5b6bb647ba23a99e7890f096da2"
        self.p = "e86418b5635e3a0fcfedac3a5f1398c5d67682b1b933addb74fc19fa"
        self.img = (r"""
  _      ____   _____     _____ _   _ 
 | |    / __ \ / ____|   |_   _| \ | |
 | |   | |  | | |  __      | | |  \| |
 | |   | |  | | | |_ |     | | | . ` |
 | |___| |__| | |__| |    _| |_| |\  |
 |______\____/ \_____|   |_____|_| \_|                             
                                
               """)
        
    def login(self):
        m = 1
        while m < 2:
            
            print self.img
            
            user = raw_input("Username: ")
            password = raw_input("Password: ")
        
            
            e1_u = hashlib.sha224(user).hexdigest()
            e1_p = hashlib.sha224(password).hexdigest()
            
            if e1_u == self.u and e1_p == self.p:
                m = 3
            else:
                print "[-]Usuario o contraseña incorrecto"
                os.system("clear") 
            
i = interface()
i.login()
        
        
