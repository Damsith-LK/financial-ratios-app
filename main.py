from flask import Flask, render_template
import datetime
from ratios import ratios_dict

app = Flask(__name__)
year = datetime.datetime.now().year

@app.route("/")
def home():
    return render_template("index.html", year=year)

@app.route("/ratio/<string:ratio>")
def ratio(ratio):
    if ratio in ratios_dict:
        name = ratios_dict[ratio]["name"]
        description = ratios_dict[ratio]["description"]
    return render_template("ratio.html", ratio_name=name, ratio_description=description, year=year)

if __name__ == "__main__":
    app.run(debug=True, port=5002)