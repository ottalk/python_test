from libs.bottle import route, run

@route('/hello')
def hello():
    return "Hello World X!"

run(host='0.0.0.0', port=8080, debug=True)