import logging
import inspect
import os

def custom_logger(file_level=logging.DEBUG, console_level=logging.INFO):
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)  # Capture all messages, handlers decide what to write

    # Prevent adding handlers multiple times
    if not logger.handlers:
        # Create logs directory
        os.makedirs("logs", exist_ok=True)
        log_file = os.path.join("logs", f"{logger_name}.log")

        # Console handler
        if console_level is not None:
            ch = logging.StreamHandler()
            ch.setLevel(console_level)
            ch.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
            logger.addHandler(ch)

        # File handler
        fh = logging.FileHandler(log_file, mode='a', encoding='utf-8')
        fh.setLevel(file_level)
        fh.setFormatter(logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        ))
        logger.addHandler(fh)

        # Separator for each test
        logger.info("\n" + "=" * 80 + f"\nNEW TEST: {logger_name}\n" + "=" * 80)

    return logger
