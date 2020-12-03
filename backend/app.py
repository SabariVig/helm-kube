from datetime import datetime
from flask import Flask

app = Flask(__name__)


@app.route('/')
def helloIndex():
    return 'Hello World from Sabari and Suhaas!'

@app.route('/time')
def get_current_time():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  return {'time': current_time}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
