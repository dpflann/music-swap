#from google.appengine.ext import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
import cgi
import os
import jinja2
import webapp2
import datetime
from models import Entry

template_directory = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_directory), autoescape=True) #autoescaping for escaping html 

##DB METHODS
def create_entry(original_urls, oembed_urls, oembed_media_urls, body, author, email, date, tags):
  return Entry(original_urls = original_urls,
      oembed_urls = oembed_urls,
      oembed_media_urls = oembed_media_urls,
      body = body,
      author = author,
      email = email,
      date = date,
      tags = tags)

def get_entries(update=False):
  query = db.GqlQuery("SELECT * FROM Entry ORDER BY created DESC")
  return list(query)

def add_entry(entry):
  entry.put()

## HANDLERS

class Handler(webapp2.RequestHandler):
  def write(self, *a, **kw):
    self.response.out.write(*a, **kw)
  
  def render_string(self, template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

  def render(self, template, **kw):
    self.write(self.render_string(template, **kw))


class MainPage(Handler):
  def render_front(self):
    entries = get_entries()
    self.render("index.html", entries = entries)

  def get(self):
    self.render_front()

  def post(self):
    pass

class CreateEntry(Handler):
  def render_front(self):
    entry = create_entry(["http://vimeo.com/12622016"],
        ["http://vimeo.com/12622016"],
        ["<iframe src=\"http://player.vimeo.com/video/12622016/\" width=\"560\" height=\"400\" frameborder=\"0\" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>"],
        "The Music Scene by Blockhead, wonderous vivid music video!",
        "Dan Flan",
        "danflan@dmail.com",
        datetime.datetime(2012, 11, 14, 5, 6),
        ["pirates", "swashbuckling", "turntablism", "Blockhead"])
    add_entry(entry)

    self.render("creating.html")
  
  def get(self):
    self.render_front()

  def post(self):
    pass

application = webapp2.WSGIApplication([
                                    ('/', MainPage),
                                    ('/create', CreateEntry)],
                                    debug=True)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
