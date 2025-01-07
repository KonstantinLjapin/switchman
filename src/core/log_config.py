import logging


def create_log():
    log_file_path = 'debug.log'
    try:
        with open(log_file_path, 'r+') as f:
            pass
    except IOError:
        with open(log_file_path, 'w+') as f:
            pass
    file_log = logging.FileHandler(filename=log_file_path)
    console_out = logging.StreamHandler()
    logging.basicConfig(level=logging.DEBUG, handlers=(file_log, console_out),
                        format="%(asctime)s %(levelname)s %(message)s")
    return logging.getLogger()


loger = create_log()
