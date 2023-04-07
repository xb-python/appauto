import os


class AutoNative:

    def __init__(self, phone):
        self.phone = phone

    def appStart(self, androidPackage):
        os.popen(f'adb shell am start -W {androidPackage}')

    def appClear(self, androidPackage):
        self.phone.app_clear(androidPackage)

    def appWait(self, androidPackage):
        self.phone.app_wait(androidPackage)

    def appStop(self, androidPackage):
        self.phone.app_stop(androidPackage)

