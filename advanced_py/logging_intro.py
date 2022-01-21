import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %('
                           'message)s',
                    level=logging.DEBUG)

logger = logging.getLogger('test_logger')

logger.info('This will not show up')
logger.warning('This will show up')
logger.debug('This is a debug msg')
logger.critical('A critical error')


"""
DEBUG <- least important
INFO
WARNING
ERROR
CRITICAL <- high priority!
"""