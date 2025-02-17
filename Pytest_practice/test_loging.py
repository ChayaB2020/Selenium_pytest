import logging

logger=logging.getLogger(__name__)
logging.basicConfig(filename='logger_file.log',filemode='a',format='%(asctime)s : %(levelname)s :%(name)s :%(message)s', level=logging.INFO)

logger.debug("This is the debug logger")
logger.info("this is the info logger")
logger.warning("This is the warning logger")
logger.error("This is the error logger")
logger.critical("this is the critical logger")
