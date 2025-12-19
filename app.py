from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://api.mymemory.translated.net/get"

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = ""
    error = ""
    if request.method == 'POST':
        text = request.form.get('english', '').strip()
        if not text:
            error = "Please enter English text."
        else:
            params = {'q': text, 'langpair': 'en|ta'}
            try:
                r = requests.get(API_URL, params=params, timeout=5)
                result = r.json()
                translation = result['responseData']['translatedText']
            except:
                error = "Translation failed. Try again."
    return render_template('index.html', translation=translation, error=error)

if __name__ == "__main__":
    app.run(debug=False)
