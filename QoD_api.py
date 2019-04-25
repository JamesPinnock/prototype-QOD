import requests
# import pprint
from datetime import date
from flask import Flask, render_template

app = Flask(__name__)

api_reponse = requests.get("https://quotes.rest/qod")
print(api_reponse)
Qod_text = api_reponse.json( )

today = date.today()

day_of_week = today.strftime("%A")

text = Qod_text['contents']['quotes'][0]['quote']
# print(type(text))
# print(text)

@app.route("/")
def hello():
    return render_template("main_page.html", text=text, day_of_week=day_of_week)

if __name__ == "__main__":
    app.run(debug=True)
