from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # Construct filename and pass to Pandas
    filename = "weather-data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    # Access date value from url and look up temperature / 10
    temperature = df.loc()[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }


if __name__ == "__main__":
    app.run(debug=True, port=5000)
