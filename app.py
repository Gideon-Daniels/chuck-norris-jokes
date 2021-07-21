from flask import Flask , render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()
    jokes = response['value']
    icon = f"{response['icon_url']}"
    joke_id = response['id']
    joke_updated = response['updated_at']
    return response


if __name__ == "__main__":
    app.run()
    app.debug = True
