from datetime import datetime
from classes.bcolors import bcolors


class log:
    @staticmethod
    def info(text: str):
        print(f"{bcolors.OKCYAN}[INFO]{bcolors.ENDC} [{log.get_current_time()}] {text}")

    @staticmethod
    def warning(text: str):
        print(
            f"{bcolors.WARNING}[WARNING]{bcolors.ENDC} [{log.get_current_time()}] {text}"
        )

    @staticmethod
    def error(text: str):
        print(f"{bcolors.FAIL}[ERROR]{bcolors.ENDC} [{log.get_current_time()}] {text}")

    @staticmethod
    def get_current_time():
        dt_string = datetime.now().strftime("%H:%M:%S")
        return dt_string

