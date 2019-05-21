from flask import Flask, redirect, render_template

url_dict = {
    'google': 'https://google.com',
    'example': 'https://example.com'
}


app = Flask(__name__)


def get_page(short_name):
    try:
        return url_dict[short_name]
    except KeyError:
        return None


@app.route('/<short_name>')
def redirection_page(short_name):
    page_from_db = get_page(short_name)
    if not page_from_db:
        return render_template('404.html'), 404
    else:
        return redirect(page_from_db)


@app.route('/')
def welcome():
    return render_template('welcome.html')