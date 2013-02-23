from google.appengine.ext import db
import webapp2

class Entry(db.Model):
  body = db.TextProperty()
  author = db.TextProperty()
  email = db.EmailProperty() #"gordon@example.com"
  date = db.DateTimeProperty(required = True)
  created = db.DateTimeProperty(auto_now_add = True)
  original_urls = db.StringListProperty(required = True)
  oembed_urls = db.StringListProperty()
  oembed_media_urls = db.StringListProperty()



