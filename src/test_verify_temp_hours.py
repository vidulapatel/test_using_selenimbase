""" Testing/Automation Task done with  EventFiringWebDriver with AbstractEventListener """

from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.events import AbstractEventListener
from seleniumbase import BaseCase
import time
from datetime import datetime,timedelta
import re


class MyListener(AbstractEventListener):

    def before_navigate_to(self, url, driver):
        print("Before navigating to: %s" % url)

    def after_navigate_to(self, url, driver):
        print("After navigating to: %s" % url)

    def before_find(self, by, value, driver):
        print('Before find "%s" (by = %s)' % (value, by))

    def after_find(self, by, value, driver):
        print('After find "%s" (by = %s)' % (value, by))

    def before_click(self, element, driver):
        print('Before clicking on element with text: "%s"' % element.text)

    def after_click(self, element, driver):
        print("Click complete!")


class EventFiringTestClass(BaseCase):

    def test_event_firing_webdriver(self):
        self.driver = EventFiringWebDriver(self.driver, MyListener())
        self.driver.delete_all_cookies()
        # Go to "https://darksky.net/"
        self.open("https://darksky.net/")

        # Enter 10001 in search location field and click on Search button
        self.update_text("#searchForm > input[type=text]", "10001\n")

        # Now find Current temperature element from currentDetailsWrapper
        current_t = self.get_text("#title > span.currently > span.desc.swap > span.summary.swap")
        current_temp = ''.join(filter(str.isdigit, current_t))
        print("\nCurrent Temperature for 10001 = %s\n" % current_temp)

        # Now find hours and temperatures from timeline
        hours = (self.get_text("#timeline > div > div.hours")).split('\n')
        print(hours)
        timeline_temps = (self.get_text("#timeline > div > div.temps")).split('\n')
        temps = []
        for elem in timeline_temps:
            temps.append(''.join(filter(str.isdigit, elem)))
        print(temps)

        lowest_from_timeline = min(temps)
        highest_from_timeline = max(temps)
        # Verify current temperature is not less than the lowest value from timeline temperature
        self.assertGreaterEqual(current_temp, lowest_from_timeline)
        # Verify current temperature is not greater than the highest value from timeline temperature
        self.assertLessEqual(current_temp, highest_from_timeline)

        # Get current time
        current_time = datetime.now()
        current_hour = int(current_time.strftime("%H"))
	# check if timeline hours increase by 2hrs after current_hour for next 24 hrs
        self.assertEqual(len(hours), 12)
        for i in range(1, len(hours)):
            next_hour = (current_hour + 2) % 12
            if next_hour == 0:
                next_hour = 12
            self.assertEqual(next_hour, int(''.join(filter(str.isdigit, hours[i]))))
            current_hour = next_hour
        print("Done")
        self.driver.close()
