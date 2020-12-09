import logging


class GenerateLog:

    @staticmethod
    def logg():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename='./logs/test_logs.log',format='%(asctime)s : %(levelname)s: %(message)s', datefmt='%m %d %Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
