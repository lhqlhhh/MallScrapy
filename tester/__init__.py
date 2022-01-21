import logging
import time


class Tester:
    def __init__(self):
        self.a = "tester"

    def run(self):
        print("stdout test")
        logging.info("start sleeping")
        time.sleep(2)
        logging.info("after 10 seconds")
        logging.info("this is just a " + self.a)
        print("stdout test end")
