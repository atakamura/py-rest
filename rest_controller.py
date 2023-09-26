from flask import Flask, jsonify, request
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/current_date', methods=['GET'])
def get_current_date():
    timezone = request.args.get('timezone', default='UTC', type=str)
    
    # Ensure the provided timezone is valid
    if timezone not in pytz.all_timezones:
        return jsonify(error="Invalid timezone"), 400

    current_time = datetime.now(pytz.timezone(timezone))
    formatted_date = current_time.strftime('%Y-%m-%d %H:%M:%S')
    
    return jsonify(date=formatted_date, timezone=timezone)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
