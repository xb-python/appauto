import os
from loguru import logger
from webdriver_manager.chrome import ChromeDriverManager

# 运行在远程服务端
def getChromeDriverPath():
    # 下载chrome驱动
    chromedriverpath = ChromeDriverManager(path='./', ).install()
    logger.debug(f'chromedriver路径:{chromedriverpath}')

    # 启动 chrome 远程服务 指定端口，指定ip
    os.system(f'{chromedriverpath} --port=9515 --allowed-ips=127.0.0.1')

if __name__ == '__main__':
    getChromeDriverPath()