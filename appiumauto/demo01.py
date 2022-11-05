
# 导包
import time
from appium import webdriver


def demo_appium():

    # 配置参数
    desired_caps = {}  # 构造一个空字典
    desired_caps['platformName'] = 'Android'  # 系统  必须指明
    # desired_caps['androidDeviceSerial'] = 'EJLDU16913016165'  # 设备名称  必须指明
    # desired_caps['androidDeviceSerial'] = 'LGUS9921650a76b'  # 设备名称  必须指明
    desired_caps['androidDeviceSerial'] = '127.0.0.1:7555'  # 设备名称  必须指明
    desired_caps['noReset'] = True  # 启动app，保留之前数据
    desired_caps['androidUseRunningApp'] = True     # 使用已打开的app

    # 解决输入中文问题
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    desired_caps['androidPackage'] = 'com.tencent.mm'
    # desired_caps['androidPackage'] = 'com.android.browser'
    # desired_caps['androidPackage'] = 'com.android.chrome'
    # desired_caps['androidPackage'] = 'com.github.android_app_bootstrap'

    """
    appium 微信切换webview报错:
        selenium.common.exceptions.WebDriverException: Message: An unknown server-side error occurred while processing the command. Original error: invalid argument: cannot parse capability: goog:chromeOptions
        from invalid argument: unrecognized chrome option: androidDeviceSerial

    同类问题: https://github.com/appium/appium/issues/16514
    解决方法：添加参数"goog:chromeOptions"
    """
    desired_caps["goog:chromeOptions"] =  {
                    "androidDeviceSerial": desired_caps['androidDeviceSerial'],
                    # "androidPackage": desired_caps['androidPackage']
                    "androidPackage": 'com.android.browser'
                }


    """
    C:\Program Files\Appium Server GUI\resources\app\node_modules\appium\node_modules\appium-chromedriver\chromedriver\win
    """

    # 实例化driver
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
    driver.implicitly_wait(20)  # 隐式等待

    print(driver.contexts)  # 获取所有context
    for context in driver.contexts:   # 遍历获取所有context
        if (not 'WEBVIEW' in context):
            continue
        try:
            driver.switch_to.context(context)   # 切换context
        except:
            print(f'切换:{context}失败，跳过')
            continue
        windows = driver.window_handles  # 获取当前context下所有窗口
        print(windows)  # 获取所有context
        for window in windows:
            driver.switch_to.window(window)  # 切换窗口
            print('context:', context, 'window:', window, 'windowUrl:', driver.current_url)  # 打印窗口和对应url


if __name__ == '__main__':
    demo_appium()
    # demo_selenium()