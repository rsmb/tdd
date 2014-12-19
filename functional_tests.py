from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# User checks homepage 
		self.browser.get('http://localhost:8000')

		# Page title and header mention to do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# User invited to enter to do item straight away
		input_box = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			input_box.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# User types 'Buy peacock feathers'
		input_box.send_keys('Buy peacock feathers')

		# User hits enter, page updates right away
		# Page now lists "1: todo item 1..." as item in todo list
		input_box.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows)	
		)

		# Text box remains to add another item
		# User enters another to do item
		self.fail('Finish the test')

		# Page updates to show both items, text box remains

		# User gets unique URL for list, text explaining URL

		# User checks the URL, the list exists
if __name__ == '__main__':
	unittest.main(warnings='ignore')