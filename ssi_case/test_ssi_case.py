import time
import pytest
from Pages.page import SSIDivingLog, Stylish

class TestSSI():

    def test_trail(self, physical_driver_handle):
        ssi = SSIDivingLog(physical_driver_handle)
        ssi.more_btn.click()
        ssi.logbook.click()
        time.sleep(10)

    def test_stylish(self, simulator_driver_handle):
        stylish = Stylish(simulator_driver_handle)
        stylish.t_shirt_btn.click()
        stylish.cart.click()
        time.sleep(10)