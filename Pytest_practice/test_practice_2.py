from .Logging_utils import Logging_utils



class Test_logger(Logging_utils):

    def test_first(self):
        logger=self.get_log()
        logger.info("inside test_first function")