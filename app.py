from libs.bottle import route, run,request,template

@route('/hello')
def hello():
    return "Hello World XXX!"

@route('/queryvars')
def display_forum():
    id = request.query.id
    page = request.query.page or '1'
    return template('Forum ID: {{id}} (page {{page}})', id=id, page=page)


run(host='0.0.0.0', port=8080, debug=True)