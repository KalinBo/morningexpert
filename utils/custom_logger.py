import logging
import inspect

def custom_logger(file_level, console_level = None):
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    if console_level != None:
        ch = logging.StreamHandler()
        ch.setLevel(console_level)
        ch_format = logging.Formatter('%(asctime)s - %(message)s')
        ch.setFormatter(ch_format)
        logger.addHandler(ch)
    fh = logging.FileHandler("{0}.log".format(logger_name))
    fh.setLevel(file_level)
    fh_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fh.setFormatter(fh_format)
    logger.addHandler(fh)

    return logger