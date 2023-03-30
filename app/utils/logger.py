import logbook
from app import pity
from .decorator import SingletonDecorator


@SingletonDecorator
class Log(object):
    def __init__(self, name='pity', filename=pity.config['LOG_NAME']):
        self.handler = logbook.FileHandler(filename, encoding='utf-8')
        # 将日志时间设置为本地时间
        logbook.set_datetime_format('local')
        self.logger = logbook.Logger(name)
        self.handler.push_application()

    def info(self, *args, **kwargs):
        return self.logger.info(*args, **kwargs)

    def error(self, *args, **kwargs):
        return self.logger.error(*args, **kwargs)

    def warning(self, *args, **kwargs):
        return self.logger.warning(*args, **kwargs)

    def debug(self, *args, **kwargs):
        return self.logger.debug(*args, **kwargs)