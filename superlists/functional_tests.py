from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicity_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
	
	# Edith had heard about a cool new online to-dp app. She goes
	# to check out it's homepage
        self.browser.get('http://localhost:8000')

	# She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

	# She is invited to enter a to-do item straight away

	# She types "buy peacock feathers" into a text box 

	# When she hits enter, the page updates, and now the page lists
	# 1) buy peacock feathers as an item on the to-do list

	# There is still a text box inviting her to add another item. 
	# She enters "Use peacock feathers to make a fly"
	
	# The page updates againm and now shows both items on her list

	# Edith wonders whether the site will remember her list. Then 
	# She sees that the site has created a unique URL for her --there
	# is some explanatory text to that effect

	# She visits that URL - her to-do list is there. 

	# She is satisfied


if __name__ == '__main__':
    unittest.main(warnings='ignore')