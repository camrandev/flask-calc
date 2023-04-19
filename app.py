# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


#4 routes - add, sub, mult, div do them seperate then combine latter

operations = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

def perform_operation(req_operation, request):
    """performs actual mathemetical operation, utilized by route handlers"""
    operation = operations[req_operation]

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return operation(a, b)


@app.get('/<req_operation>')
def handle_request(req_operation):
    """handles requests sent directly to /operation endpoint"""
    print(f"{request}")
    result = perform_operation(req_operation, request)
    return str(result)


@app.get('/math/<req_operation>')
def handle_all(req_operation):
    """handles requests sent to math/operation endpoint"""
    result = perform_operation(req_operation, request)
    return str(result)

    # print(f"{request.args}")
    # return(f"{method}")


# @app.get('/math/add')
# def addition():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))

#     return f"{add(a, b)}"

# @app.get('/math/sub')
# def subtraction():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))

#     return f"{sub(a, b)}"

# @app.get('/math/div')
# def division():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))

#     return f"{div(a, b)}"

# @app.get('/math/mult')
# def multiplication():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))

#     return f"{mult(a, b)}"