from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/time')
def get_current_time():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  return {'time': current_time}
