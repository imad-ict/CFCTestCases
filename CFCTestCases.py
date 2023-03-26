import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestApp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login_valid_credentials(self):
        driver = self.driver
        driver.get("https://your-web-app-url.com/login")

        # Enter valid credentials
        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        username.send_keys("valid_username")
        password.send_keys("valid_password")

        # Click the login button
        login_button = driver.find_element_by_name("login")
        login_button.click()

        # Wait for the dashboard page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dashboard")))

        # Check if the user has been redirected to the dashboard page
        self.assertEqual(driver.current_url, "https://your-web-app-url.com/dashboard")

    def test_login_invalid_credentials(self):
        driver = self.driver
        driver.get("https://your-web-app-url.com/login")

        # Enter invalid credentials
        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        username.send_keys("invalid_username")
        password.send_keys("invalid_password")

        # Click the login button
        login_button = driver.find_element_by_name("login")
        login_button.click()

        # Wait for the error message to appear
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "error-message")))

        # Check if an error message is displayed
        error_message = driver.find_element_by_id("error-message")
        self.assertTrue(error_message.is_displayed())

    def test_signup_valid_details(self):
        driver = self.driver
        driver.get("https://your-web-app-url.com/signup")

        # Enter valid signup details
        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        email = driver.find_element_by_name("email")
        username.send_keys("new_username")
        password.send_keys("new_password")
        email.send_keys("new_email@example.com")

        # Click the signup button
        signup_button = driver.find_element_by_name("signup")
        signup_button.click()

        # Wait for the confirmation message to appear
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "confirmation-message")))

        # Check if a confirmation message is displayed
        confirmation_message = driver.find_element_by_id("confirmation-message")
        self.assertTrue(confirmation_message.is_displayed())

    def test_navigate_to_profile_after_login(self):
        driver = self.driver
        driver.get("https://your-web-app-url.com/login")

        # Log in with valid credentials
        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        username.send_keys("valid_username")
        password.send_keys("valid_password")
        login_button = driver.find_element_by_name("login")
        login_button.click()

               # Wait for the dashboard page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dashboard")))

        # Click the profile link or button
        profile_link = driver.find_element_by_id("profile-link")
        profile_link.click()

        # Wait for the profile page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "profile")))

        # Check if the user has been redirected to the profile page
        self.assertEqual(driver.current_url, "https://your-web-app-url.com/profile")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

