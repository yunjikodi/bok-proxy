// app.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/bokdata')
def proxy():
    stat_code = request.args.get('stat_code')
    start = request.args.get('start')
    end = request.args.get('end')
    cycle = 'M'

    api_key = "여기에_당신의_API_KEY_입력"

    url = f"https://ecos.bok.or.kr/api/StatisticSearch/{api_key}/json/kr/1/100/{stat_code}/{cycle}/{start}/{end}"
    res = requests.get(url)

    return jsonify(res.json())

if __name__ == "__main__":
    app.run()
