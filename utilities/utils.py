import softest
import logging
import inspect

class Utils(softest.TestCase):
    def assert_list_item(self,list,value):
        #log = self.custom_logger()
        #log.info('Step 10 : Verify Filter works file')
        for stops in list:
            #log.debug("The text is:" + stops.text)
            self.soft_assert(self.assertIn,value,stops.text)
            if value in stops.text:
                print("test passed")
            else:
                print("test failed")
        self.assert_all()

    def custom_logger(loglevel=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(loglevel)
        fh = logging.FileHandler("automation.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

