#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
this is the main program 
to run it please use this cmd  python main.py
this method will call 

1 - process_xml.py and do the following (steps 1 qand 2)

 - get file and check if it exisits 
 - parse xml and get root
 - validate xml 
 - store graph model  to db (using repository pattern)


2 - process_json_request.py and do the followings (step 5)

 - get json input (somewhere)
 - parse json 
 - get graph object (repository - ORM - DB)
 - get paths for given query
 - format json output
 - send back (print) json output

"""


import process_xml
import process_json_request

def main():
    process_xml.process("graph.xml")
    response = process_json_request.process()
    print (response)

if __name__ == '__main__':
    main()