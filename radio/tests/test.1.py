import time
import logging
import datetime

logging.basicConfig(filename="logs/test.1.log", encoding="utf-8", level=logging.DEBUG)
logging.info("test.1.py started " + str(datetime.datetime.now()))

time.sleep(3)

logging.info("test.1.py finished " + str(datetime.datetime.now()))
quit()
