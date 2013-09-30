'''Functional tests using Selenium'''

from nose.tools import *
from functional_tests.utils import SeleniumTestCase, CustomWebDriver

from base.tests.factories import UserFactory

class TestAUser(SeleniumTestCase):
    def setUp(self):
        # Create a user
        self.user = UserFactory()
        self.driver = CustomWebDriver()
    
    def tearDown(self):
        self.driver.quit()

    def test_can_login(self):
        '''Test that a user can login from the home page.
        '''
        # go to home page
        self.open('/')
        # type in login info
        self.driver.find_css('input[name="username"]').\
                    send_keys(self.user.username)
        self.driver.find_css('input[name="password"]').\
                    send_keys('abc')
        # submit
        self.driver.click_submit()
        # user is now authenticated
        assert_true(self.user.is_authenticated())
        # page shows that user is logged in
        assert_in('Logged in', self.driver.body_text())