from run import app
import unittest

class FlaskTestCase(unittest.TestCase):

	# Checking for correct flask setup

	def test_home(self):
		
		tester = app.test_client(self)
		# response = tester.get('/', follow_redirects = True)
		response = tester.get('/', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
	unittest.main()