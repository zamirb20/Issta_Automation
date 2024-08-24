from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time

WEBSITE = "https://www.issta.co.il"
chrome_driver_path = "C:\\Users\\user\\Desktop\\python_angela\\chromedriver.exe"


# Function to open the homepage
def open_homepage(driver, url):
    driver.get(url)
    time.sleep(2)  # Wait for the homepage to load


# Function to set a destination
def set_destination(driver, destination):
    try:
        # Locate the destination input field;
        destination_input = driver.find_element("xpath", "/html/body/div[2]/div/div[2]/div/div[2]/app-search-engine/div/se-group/div[1]/div/div/se-tabs/div/se-tab[1]/div/div/se-packages/se-packages-container/div/div[2]/div[1]/se-packages-form/form/div/div[1]/div/div")
        time.sleep(1)  # Wait a bit
        destination_input.send_keys(destination)

    except NoSuchElementException:
        print("Destination input field not found!")


def set_dates(driver, departure_date, return_date):
    try:
        # Locate the dates input fields;
        departure_input = driver.find_element("xpath", "/html/body/div[2]/div/div[2]/div/div[2]/app-search-engine/div/se-group/div[1]/div/div/se-tabs/div/se-tab[1]/div/div/se-packages/se-packages-container/div/div[2]/div[1]/se-packages-form/form/div/div[2]/div[1]/se-packages-datepicker-desktop/div/div[4]/div[2]/div/div[2]/table[1]/tbody/tr[5]/td[1]/div/span[2]" )
        time.sleep(1)  # Wait a bit
        return_input = driver.find_element("xpath", "/html/body/div[2]/div/div[2]/div/div[2]/app-search-engine/div/se-group/div[1]/div/div/se-tabs/div/se-tab[1]/div/div/se-packages/se-packages-container/div/div[2]/div[1]/se-packages-form/form/div/div[2]/div[1]/se-packages-datepicker-desktop/div/div[4]/div[2]/div/div[2]/table[2]/tbody/tr[4]/td[1]/div/span[1]")
        time.sleep(1)  # Wait a bit
        departure_input.send_keys(departure_date)
        time.sleep(1)  # Wait a bit
        return_input.send_keys(return_date)

    except NoSuchElementException:
        print("dates input field not found!")


def set_Passenger_details(driver, details):
    try:
        # Locate the passengers details input fields;
        Passenger_details = driver.find_element("xpath", "/html/body/div[2]/div/div[2]/div/div[2]/app-search-engine/div/se-group/div[1]/div/div/se-tabs/div/se-tab[1]/div/div/se-packages/se-packages-container/div/div[2]/div[1]/se-packages-form/form/div/div[2]/div[2]/se-packages-passengers-picker/div/div[1]" )
        time.sleep(1)  # Wait a bit
        Passenger_details.send_keys(details)

    except NoSuchElementException:
        print("Passengers details input field not found!")


# Function to click the search button and assert the results
def click_search_and_assert(driver):
    try:
        # Locate and click the search button
        search_button = driver.find_element("xpath", "/html/body/div[2]/div/div[2]/div/div[2]/app-search-engine/div/se-group/div[1]/div/div/se-tabs/div/se-tab[1]/div/div/se-packages/se-packages-container/div/div[2]/div[1]/se-packages-form/form/div/div[2]/div[3]/div/form-button/button")
        search_button.click()

        # Wait for the search results to load
        time.sleep(10)

        # Assertion: Check if the results page is loaded by verifying the presence of a specific element
        results_element = driver.find_element("xpath", "/html/body/div[2]/div/main/div")
        assert results_element.is_displayed(), "Search results not displayed!"

        print("Search was successful and results are displayed.")

    except NoSuchElementException:
        print("Search button or results element not found!")
    except AssertionError as e:
        print(e)


# Set up the WebDriver and open the homepage
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
open_homepage(driver, WEBSITE)

# Set the destination
set_destination(driver, "Baku")  # Replace with the desired destination

# Set the dates
set_dates(driver, "25-08-24", "29-08-24")

# Set the Passengers Details
set_Passenger_details(driver, "2 Adults")

# Click on the search button and assert the results
click_search_and_assert(driver)

# Clean up and close the browser
driver.quit()
