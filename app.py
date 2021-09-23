# the main problem is receiving data from user and then use it as a visualization items,
# and then need to delete them, will delete instead of saving data over time.
# data will be csv and images
# need to check streamlit documentation if i can do this other wise it will be a flask app.
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        return render_template('vis.html')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
