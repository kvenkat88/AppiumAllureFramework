import logging
import os
from appium import webdriver
from utility.framework.config_utility import ConfigUtility
from utility.framework.logger_utility import custom_logger

class DriverFactory:
    """
    This class contains the reusable methods for getting the driver instances
    """
    log = custom_logger(logging.INFO)
    config = ConfigUtility()

    def __init__(self, platform):
        self.platform = platform
        self.cur_path = os.path.abspath(os.path.dirname(__file__))
        self.prop = self.config.load_properties_file()

    def get_driver_instance(self):

        if self.platform == "android":

            app_location = os.path.join(self.cur_path, r"../../binary/android/", self.prop.get('Cap_Android', 'app_name'))

            desired_caps = {
                'automationName': self.prop.get('Cap_Android', 'automation_name'),
                'deviceName': self.prop.get('Cap_Android', 'device_name'),
                'udid': self.prop.get('Cap_Android', 'ud_id'),
                'platformName': 'Android',
                'platformVersion': self.prop.get('Cap_Android', 'platform_version'),
                'appPackage': self.prop.get('Cap_Android', 'app_package'),
                'appActivity': self.prop.get('Cap_Android', 'app_activity'),

                # If app_package and app_activity is provided then no need to provide .apk file path as Appium Documentation
                'app': app_location,
                'fullReset': self.prop.get('Cap_Android', 'full_reset'),
                'autoGrantPermissions': self.prop.get('Cap_Android', 'auto_grant_permissions'),

                'unicodeKeyboard': self.prop.get('Cap_Android', 'unicode_keyboard'),
                'resetKeyboard': self.prop.get('Cap_Android', 'reset_keyboard'),

                # Speed up the appium tests
                'skipDeviceInitialization': self.prop.get('Cap_Android', 'skip_device_Init'),
                'skipServerInstallation': self.prop.get('Cap_Android', 'skip_server_Installation'),
            }

            driver = webdriver.Remote(
                command_executor=self.prop.get('Selenium_Grid_or_Appium_Remote_Server_Address', 'appium_server'),
                desired_capabilities=desired_caps)

            return driver

        elif self.platform == "ios":
            pass