import logging

LEVEL = 'DEBUG'
# FORMAT = '%(asctime)-15s - %(thread)d - %(filename)s - %(message)s'
# FORMAT = '%(asctime)-15s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s'
FORMAT = '%(asctime)-15s - %(levelname)s - %(filename)s.%(funcName)s :%(lineno)d - %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('LaundryViewer')
logger.setLevel(LEVEL)
