from flask import Flask

app = Flask(__name__)

@app.route('/',  methods=['GET'], strict_slashes=False)
def index():
  return '<h1>Hello, World!</h1>'

if __name__ == '__main__':
    app.run(debug=True, port='8080', host='0.0.0.0')
