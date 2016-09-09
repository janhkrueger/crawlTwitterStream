#!/usr/bin/env python2.7
# encoding: utf-8


import sys, StringIO, os, json
import psycopg2
import ConfigParser
from pprint import pprint


def main():
  # Read db credentials and open connection
	conf = ConfigParser.ConfigParser()
	conf.read(["/var/games/KillReporter/init.ini", "init_local.ini"])

	db_schema = conf.get("GLOBALSPSQL","edb_name")
	db_IP = conf.get("GLOBALSPSQL","edb_host")
	db_user = conf.get("GLOBALSPSQL","edb_user")
	db_pw = conf.get("GLOBALSPSQL","edb_pw")
	db_port = int(conf.get("GLOBALSPSQL","edb_port"))
	db = psycopg2.connect(database =db_schema, host=db_IP, user=db_user, password=db_pw)
	cursor = db.cursor()

	try:
          # Get all tweets
          try:
            cursor.execute("SELECT tweetid, tweetcontent FROM twitter.tweets ORDER BY tweetid ASC")
          except:
            # could not fetch the tweets
            sys.exit(11)

          # try writing all tweets in separate files
          # if a file exists: overwrite
          try:
            for row in cursor:
              filename = '%s.txt' % row[0]
              try:
                with open( filename, 'w' ) as outfile:
                  json.dump(row[1], outfile)
                  outfile.closed
              except:
                print('Could not write Tweet %s') % row[0]
          except:
            # unable to write the tweets to the filesystem
            sys.exit(8)
     
        except:
          # omg!
          sys.exit(8)
	
        cursor.close()
        db.close()

if __name__ == "__main__":
	main()
