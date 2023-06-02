from flask import Flask,jsonify
from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello_world(): 
    return "Hello World"
#Here onwards you you can write your way of creating a function
@app.route("/odd_even/<int:n>") #pass on the same function name
def odd_even(n):
    copy_n=n
    if n%2==0:
        result={
            "Even":"Yes",
            "Odd":"No",
        }
    if n%2!=0:
        result={
            "Even":"No",
            "Odd":"Yes",
        }
    return jsonify(result)
if __name__=="__main__": #It will start the server
    app.run(debug=True) #debug=True will run it dev enviourment

    