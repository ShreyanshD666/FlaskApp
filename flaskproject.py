from flask import Flask,jsonify, request
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'Name': 'Shreyansh',
        'Contact': '9999978787', 
        'done': False
    },
    {
        'id': 2,
        'Name': 'Keshav',
        'Contact': '9811588898', 
        'done': False
    }
]

@app.route("/")
def helloWorld():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def addTask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    tasks.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)