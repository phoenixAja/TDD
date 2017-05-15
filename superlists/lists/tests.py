from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.conf import settings
if not settings.configured:
	settings.configure()
from lists.models import Item


class HomePageTest(TestCase):

	# test to make sure '/'' resolves to the home page
	def test_root_url_resolves_to_home_page(self):

		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		#http request object, what django sees when a users browser asks for a page

		request = HttpRequest() 

		#we pass above to home_page view, which gives us a response, then 
        #we assert that the .content of the response - which is the HTML we are
        #sending to the user has certain properties
		response = home_page(request) 
		expected_html = render_to_string('home.html')

        # decode converts response.content bytes into 
        # python unicode string, (comparing strings w/
        # strings instead of comparing bytes
		self.assertEqual(response.content.decode(), expected_html) 
                                                                   
        #we want it to start with an <html> tag which 
        #gets closed at the end. notice raw bytes
        #self.assertTrue(response.content.startswith(b'<html>')) 
                                                                
        #we want a title tag somewhere in the middle
        #with the words to-do list
        #self.assertIn(b'<title>To-Do Lists</title>', response.content)      
        #self.assertTrue(response.content.strip().endswith(b'</html>'))

	def test_home_page_can_save_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new list item'

		response = home_page(request)

		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'A new list item')

		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

	def test_home_page_only_saves_items_when_necessary(self):
		request = HttpRequest()
		home_page(request)
		self.assertEqual(Item.objects.count(),0)


class ItemModelTest(TestCase):

	# testing data storage and retrieval
	def test_saving_and_retrieving_items(self):

		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the second'
		second_item.save()

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'The first (ever) list item')
		self.assertEqual(second_saved_item.text, 'Item the second')
