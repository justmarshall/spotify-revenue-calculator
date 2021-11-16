from flask import Flask
from flask.globals import request
from flask.templating import render_template

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def calculate():
    revenue = ""
    period_display = ""
    stream_count = ""
    if request.method=='POST' and 'streams' in request.form: 
        streams = float(request.form.get("streams"))
        period = request.form.get("period")
        if period == "monthly":
            revenue = "{:,}".format(round(30*(streams * 0.004)))
            period_display = "Per Month"
            stream_count = "{:,}".format(int(streams))
        elif period == "yearly":
            revenue = "{:,}".format(round(364*(streams * 0.004)))
            period_display = "Per Year"
            stream_count = "{:,}".format(int(streams))
    return render_template("index.html", revenue=revenue, period_display=period_display, stream_count=stream_count)