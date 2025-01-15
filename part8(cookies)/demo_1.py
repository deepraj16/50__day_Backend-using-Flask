from flask import Flask ,make_response,request

app =Flask(__name__)

@app.route("/")
def home():
    response =make_response("<h1>wellocme to the home page!!</h1>")
    return response

@app.route("/set_cookie")
def set_cookies():
    response=make_response("<h1>Wellcome to the Set Cookies Page!!</h1>")
    response.set_cookie("cookie_name","cookie_name")
    return response

@app.route("/get_cookie")
def get_cookies():
    value=request.cookies.get("cookie_name")
    response=make_response(f"<h1>The cookies value is <i>{value}</i>!!</h1>")
    return response


if __name__== "__main__" :
    app.run(debug=True)



