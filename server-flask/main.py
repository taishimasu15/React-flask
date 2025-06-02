from flask import Flask 
from flask_cors import CORS 

app = Flask (__name__)
CORS(app)


@app.route("/")
def hello_world(): 
    return "te amo mi amor, me quiero casar contigo"

@app.route("/api/users")
def get_users ():
    return{
        "users" : ["Alice", "Bob", "Charlie"]
    }

@app.route("/api/fruits")
def get_fruits ():
    return{
        "fruits" : ["Cambur", "Cereza", "Uvita"]
    }

if __name__ == "__main__":
    app.run(debug=True) #by default, Flask runs on port 5000