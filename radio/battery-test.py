import logging
import datetime
import time

def curr_time():
    return str(datetime.datetime.now())


def main():
	logging.basicConfig(filename="logs/battery-test.log", encoding="utf-8", level=logging.DEBUG)

	logging.info(f"Starting @ {curr_time()}")
	
	while True:
		logging.info(curr_time())
		time.sleep(1)

if __name__ == "__main__":
    main()