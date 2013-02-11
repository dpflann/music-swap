#from google.appengine.ext import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
import cgi
import os
import jinja2
import webapp2
from models import Entry

template_directory = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_directory), autoescape=True) #autoescaping for escaping html 


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
    self.render("index.html")

  def get(self):
    self.render_front()

  def post(self):
    pass

application = webapp2.WSGIApplication([
                                    ('/', MainPage)],
                                    debug=True)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
