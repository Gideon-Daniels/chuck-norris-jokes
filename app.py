from flask import Flask , render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()
    jokes = response['value']
    icon = f"{response['icon_url']}"
    return render_template("index.html", jokes=jokes, icon=icon)


if __name__ == "__main__":
    app.run()
    app.debug = True
