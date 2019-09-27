from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/car/')
def evaluateCar():
    pass

if __name__ == '__main__':
    app.run()
