from flask import Flask, request, make_response, render_template

app = Flask(__name__)

def load_data():
    pass



@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
