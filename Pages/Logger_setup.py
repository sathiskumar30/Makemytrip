import logging

def setup_logger(log_file='example.log', log_level=logging.DEBUG):
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # Create a file handler
    fh = logging.FileHandler(log_file, encoding='utf-8')
    # fh = logging.StreamHandler()
    fh.setLevel(log_level)

    # Create a formatter and set it for the file handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(fh)
