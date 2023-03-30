from app import pity

@pity.route('/')
def index():
    return "Hello World!"

if __name__ == '__main__':
    pity.run(host="0.0.0.0", port=8080, threaded=True)