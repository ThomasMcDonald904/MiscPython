import logging
logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s', level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S', filename="data.log")


logging.debug("Unit test")
logging.info("This is info")
logging.warning("This byte mucher is over heating")
logging.error("Something went wrong")
logging.critical("Oh no crash")