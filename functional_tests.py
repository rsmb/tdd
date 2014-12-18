from selenium import webdriver
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
		self.assertIn('To-do', self.browser.title)
		self.fail('Finish the test!')



		# User invited to enter to do item straight away

		# User hits enter, page updates right away
		# Page now lists "1: todo item 1..." as item in todo list

		# Text box remains to add another item
		# User enters another to do item

		# Page updates to show both items, text box remains

		# User gets unique URL for list, text explaining URL

		# User checks the URL, the list exists
if __name__ == '__main__':
	unittest.main(warnings='ignore')