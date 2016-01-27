#!/usr/bin/env python
#! -*- coding: utf-8 -*-
import sys,shelve
def store_person(db):
	"""
	Query user for data and store it in the shelf object
	"""
	pid=raw_input('Enter unique ID unmber:')
	person={}
	person['name']=raw_input('Enter name :')
	person['age']=raw_input('Enter age:')
	person['phone']=raw_input('Enter phone')
	db[pid]=person
def lookup_person(db):
	"""
	query person
	"""
	pid=raw_input('Enter pid:')
	print list(db[pid]['age'])

def print_help():
	print "help:"

def enter_command():
	cmd=raw_input('Enter command: ')
	cmd=cmd.strip().lower()
	return cmd

def main():
	database=shelve.open('person.dat')
	try:
		while True:
			cmd=enter_command()
			if cmd=='store':
				store_person(database)
			elif cmd=='lookup':
				lookup_person(database)
			elif cmd=='quit':
				return
	finally:
		database.close()
if __name__=='__main__':main()