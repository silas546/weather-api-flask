from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Construct a table of stations for user reference
stations = pd.read_csv("weather-data/stations.txt", skiprows=17)
filtered_stations = stations[["STAID", "STANAME                                 "]]
stations_table = filtered_stations.to_html()
@app.route("/")
def home():
    return render_template("home.html", stations=stations_table)


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # Construct filename and pass to Pandas
    filename = "weather-data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    # Access date value from url and look up temperature / 10
    temperature = df.loc()[df['    DATE'] == date]['   TG'].squeeze() / 10
    temperature_f = temperature * (9/5) + 32
    return {
        "station": station,
        "date": date,
        "temperature": temperature_f
    }


if __name__ == "__main__":
    app.run(debug=True, port=5000)
