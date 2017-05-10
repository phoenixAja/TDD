from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest() #http request object, what django sees when a users browser asks for a page

        response = home_page(request) #we pass above to home_page view, which gives us a response, then 
				      #we assert that the .content of the response - which is the HTML we are
                                      #sending to the user has certain properties

        expected_html = render_to_string('home.html')

        self.assertEqual(response.content.decode(), expected_html) # decode converts response.content bytes into 
                                                                   # python unicode string, (comparing strings w/
                                                                   # strings instead of comparing bytes

        #self.assertTrue(response.content.startswith(b'<html>')) #we want it to start with an <html> tag which 
                                                                #gets closed at the end. notice raw bytes

        #self.assertIn(b'<title>To-Do Lists</title>', response.content) #we want a title tag somewhere in the middle
								       #with the words to-do list
        #self.assertTrue(response.content.strip().endswith(b'</html>'))
