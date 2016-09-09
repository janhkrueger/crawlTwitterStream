#!/usr/bin/env python2.7
# encoding: utf-8


import sys, StringIO, os, getopt, json
import psycopg2
import ConfigParser
from pprint import pprint


def main():
	conf = ConfigParser.ConfigParser()
	conf.read(["/path/to/config/init.ini", "init_local.ini"])

	db_schema = conf.get("GLOBALSPSQL","edb_name")
	db_IP = conf.get("GLOBALSPSQL","edb_host")
	db_user = conf.get("GLOBALSPSQL","edb_user")
	db_pw = conf.get("GLOBALSPSQL","edb_pw")
	db_port = int(conf.get("GLOBALSPSQL","edb_port"))
  db = psycopg2.connect(database =db_schema, host=db_IP, user=db_user, password=db_pw)
	cursor = db.cursor()

  # Read all *.txt Files 
  mypath = '//path//to//tweets//'
  for file in os.listdir(mypath):
  	if file.endswith(".txt"):
    	id = os.path.splitext(os.path.basename(file))[0]
      tweet = open(file, 'r').read()
      jsontweet = json.loads(tweet)
	    try:
      	cursor.execute("INSERT INTO twitter.tweets (tweetid, tweetcontent) VALUES (%s, %s)", (id, json.dumps(jsontweet), ))
      	os.remove(file)
      except:
      	print ("I'm unnable to store the tweet %s", (id))
	db.commit()
	
	db.close()

if __name__ == "__main__":
	main()
