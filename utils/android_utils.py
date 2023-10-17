# def android_get_desired_capabilities():
#     return {
#         'autoGrantPermissions': True,
#         'automationName': 'uiautomator2',
#         'newCommandTimeout': 500,
#         'noSign': True,
#         'platformName': 'Android',
#         'platformVersion': '11',
#         'resetKeyboard': True,
#         'systemPort': 8301,
#         'takesScreenshot': True,
#         'udid': 'emulator-5554',
#         'connect': 10000,
#         'appPackage': 'com.ajaxsystems',
#         'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
#
#
#     }
def android_get_desired_capabilities():
    return {
        'platformName': 'Android',
        'platformVersion': '8',
        'deviceName': 'HUAWEI Y6 2018',
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity',
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'resetKeyboard': True,
        'takesScreenshot': True,
        'udid': 'GSM9X18B06G02450',
        'androidInstallTimeout': 90000,  # Увеличьте таймаут на установку до 90 секунд (или любое другое подходящее значение).
    }
