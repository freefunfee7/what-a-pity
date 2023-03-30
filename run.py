from app import pity
from app.utils.logger import Log
from datetime import datetime


@pity.route('/')
def index():
    log = Log(name='test')
    log.info('有人访问网站了')
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now)
    return now
    # return "Hello World!"

if __name__ == '__main__':
    pity.run(host="0.0.0.0", port=8080, threaded=True)