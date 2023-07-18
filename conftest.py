import pytest
from appium import webdriver

desired_caps_physical = {
    'platformName': 'iOS',
    'platformVersion': '16.5.1',  # Change this to your iOS version
    'deviceName': 'Michael iPhone 10',  # Change this to your device name
    'udid': '00008020-0005756801D8002E',  # Replace with the UDID of your device
    'automationName': 'XCUITest',
    'xcodeOrgId': '2622T7NUU7',  # Replace with your Team ID from Apple Developer account
    'xcodeSigningId': 'iPhone Developer',
    'app': 'com.divessi.ssi',  # Replace with the path to your app
    'noReset': False  # Retain app state between sessions, set it to False if you want a clean state every time
}

desired_caps_simulator = {
    'platformName': 'iOS',
    'platformVersion': '16.4',  # Change this to your iOS version
    'deviceName': 'iPhone 14 Pro',  # Change this to your device name
    'udid': '29478CD5-5FE4-46FD-A32D-B5C119B72C28',  # Replace with the UDID of your device
    'automationName': 'XCUITest',
    'xcodeOrgId': '2622T7NUU7',  # Replace with your Team ID from Apple Developer account
    'xcodeSigningId': 'iPhone Developer',
    'app': 'AppWorksSchool.Automation.STYLiSH',  # Replace with the path to your app
    'noReset': False  # Retain app state between sessions, set it to False if you want a clean state every time
}


@pytest.fixture
def physical_driver_handle():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps_physical)
    yield driver
    driver.quit()


@pytest.fixture
def simulator_driver_handle():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps_simulator)
    yield driver
    driver.quit()
