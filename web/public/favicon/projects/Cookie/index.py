import os
import logging
import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db

class MainHandler(webapp.RequestHandler):

    def get(self):
        path = self.request.path

        temp = os.path.join(
            os.path.dirname(__file__),
            'templates/' + path)

        if not os.path.isfile(temp):
            temp = os.path.join(
                os.path.dirname(__file__),
                'templates/index.html')

        outstr = template.render(temp,{})
        self.response.out.write(outstr)

    def post(self):
        temp = os.path.join(
            os.path.dirname(__file__),
            'templates/index.html')
        outstr = template.render(
            temp,
            {})
        self.response.out.write(outstr)
        
a='''class SubmitHandler(webapp.RequestHandler):

    def get(self):
        temp = os.path.join(
            os.path.dirname(__file__),
            'templates/main.html')

    def post(self):
        userinput = self.request.get('userInput')
        temp = os.path.join(
            os.path.dirname(__file__),
            'templates/main.html')
        outstr = template.render(
            temp,
            {'out_sentence': userinput})
        self.reponse.out.write(outstring)'''


def main():
    application = webapp.WSGIApplication([('/.*', MainHandler)
                                          ], debug=True)
    wsgiref.handlers.CGIHandler().run(application)
    

if __name__ == '__main__':
    main()
        
