from google.appengine.ext import db
import webapp2

class Entry(db.Model):
  def say(self, string):
    print(string)
  pass


class User(db.Model):
  pass


