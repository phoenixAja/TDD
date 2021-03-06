from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
	
	    # Edith had heard about a cool new online to-dp app. She goes
	    # to check out it's homepage
		self.browser.get('http://localhost:8000')

	    # She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

	    # She is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'),
						'Enter a To-Do item'
						) 

	    # She types "buy peacock feathers" into a text box 
	    # When she hits enter, the page updates, and now the page lists
	    # 1) buy peacock feathers as an item on the to-do list
		inputbox.send_keys('Buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)
		self.check_for_row_in_list_table('1: Buy peacock feathers')
             

	    # There is still a text box inviting her to add another item. 
	    # She enters "Use peacock feathers to make a fly
	    # The page updates againm and now shows both items on her list
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
 

	    # Edith wonders whether the site will remember her list. Then 
	    # She sees that the site has created a unique URL for her --there
	    # is some explanatory text to that effect
		self.fail('finish the test!')
	    # She visits that URL - her to-do list is there. 

	    # She is satisfied


if __name__ == '__main__':
	unittest.main(warnings='ignore')
